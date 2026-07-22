import random
import time
from collections import defaultdict
import tkinter as tk


class SnakeEnv:
    def __init__(self, grid_size=10, cell_size=30):
        self.grid_size = grid_size
        self.cell_size = cell_size
        self.reset()

    def reset(self):
        self.direction = 1  # 0=up,1=right,2=down,3=left
        self.snake = [(self.grid_size // 2, self.grid_size // 2)]
        self.food = self._spawn_food()
        self.done = False
        self.score = 0
        self.steps = 0
        return self._get_state()

    def _spawn_food(self):
        while True:
            food = (
                random.randint(0, self.grid_size - 1),
                random.randint(0, self.grid_size - 1),
            )
            if food not in self.snake:
                return food

    def _get_state(self):
        head_x, head_y = self.snake[0]
        food_x, food_y = self.food

        # Relative food position to current heading
        if self.direction == 0:  # up
            food_relative = 0 if food_y < head_y else 1 if food_y > head_y else 2
        elif self.direction == 1:  # right
            food_relative = 0 if food_x > head_x else 1 if food_x < head_x else 2
        elif self.direction == 2:  # down
            food_relative = 0 if food_y > head_y else 1 if food_y < head_y else 2
        else:  # left
            food_relative = 0 if food_x < head_x else 1 if food_x > head_x else 2

        danger_straight = self._is_collision(self._next_pos(0))
        danger_right = self._is_collision(self._next_pos(1))
        danger_left = self._is_collision(self._next_pos(-1))

        return (int(danger_straight), int(danger_right), int(danger_left), self.direction, food_relative)

    def _next_pos(self, turn):
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        dir_index = (self.direction + turn) % 4
        dx, dy = directions[dir_index]
        head_x, head_y = self.snake[0]
        return head_x + dx, head_y + dy

    def _is_collision(self, pos):
        x, y = pos
        if x < 0 or x >= self.grid_size or y < 0 or y >= self.grid_size:
            return True
        return (x, y) in self.snake[1:]

    def step(self, action):
        # action: 0 = left, 1 = straight, 2 = right
        turn = action - 1
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        self.direction = (self.direction + turn) % 4
        dx, dy = directions[self.direction]
        head_x, head_y = self.snake[0]
        new_head = (head_x + dx, head_y + dy)

        reward = -0.01
        self.steps += 1

        if (
            new_head[0] < 0
            or new_head[0] >= self.grid_size
            or new_head[1] < 0
            or new_head[1] >= self.grid_size
            or new_head in self.snake[1:]
        ):
            self.done = True
            reward = -10
            return self._get_state(), reward, self.done

        self.snake.insert(0, new_head)
        if new_head == self.food:
            self.score += 1
            reward = 10
            self.food = self._spawn_food()
        else:
            self.snake.pop()

        if self.steps > self.grid_size * self.grid_size * 4:
            self.done = True
            reward -= 5

        return self._get_state(), reward, self.done


class QLearningAgent:
    def __init__(self, alpha=0.15, gamma=0.95, epsilon=1.0, epsilon_min=0.05, epsilon_decay=0.995):
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.epsilon_min = epsilon_min
        self.epsilon_decay = epsilon_decay
        self.q_table = defaultdict(lambda: [0.0, 0.0, 0.0])

    def choose_action(self, state, explore=True):
        if explore and random.random() < self.epsilon:
            return random.randint(0, 2)
        q_values = self.q_table[state]
        return int(max(range(3), key=lambda a: q_values[a]))

    def learn(self, state, action, reward, next_state, done):
        current = self.q_table[state][action]
        if done:
            target = reward
        else:
            target = reward + self.gamma * max(self.q_table[next_state])
        self.q_table[state][action] = current + self.alpha * (target - current)

    def decay_epsilon(self):
        self.epsilon = max(self.epsilon_min, self.epsilon * self.epsilon_decay)


class SnakeGUI:
    def __init__(self, env):
        self.env = env
        self.root = tk.Tk()
        self.root.title("Reinforcement Learning Snake")
        self.canvas = tk.Canvas(
            self.root,
            width=env.grid_size * env.cell_size,
            height=env.grid_size * env.cell_size,
            bg="#111111",
            highlightthickness=0,
        )
        self.canvas.pack()

    def draw(self):
        self.canvas.delete("all")
        for x in range(self.env.grid_size):
            for y in range(self.env.grid_size):
                self.canvas.create_rectangle(
                    x * self.env.cell_size,
                    y * self.env.cell_size,
                    (x + 1) * self.env.cell_size,
                    (y + 1) * self.env.cell_size,
                    fill="#1f1f1f",
                    outline="#2e2e2e",
                )

        for x, y in self.env.snake:
            self.canvas.create_rectangle(
                x * self.env.cell_size,
                y * self.env.cell_size,
                (x + 1) * self.env.cell_size,
                (y + 1) * self.env.cell_size,
                fill="#7CFC00",
                outline="#4CAF50",
            )

        fx, fy = self.env.food
        self.canvas.create_oval(
            fx * self.env.cell_size,
            fy * self.env.cell_size,
            (fx + 1) * self.env.cell_size,
            (fy + 1) * self.env.cell_size,
            fill="#FF4136",
            outline="#FF4136",
        )
        self.canvas.update()


def train_agent(episodes=1000, max_steps=150, render_demo=False):
    env = SnakeEnv()
    agent = QLearningAgent()

    for episode in range(episodes):
        state = env.reset()
        total_reward = 0

        for _ in range(max_steps):
            action = agent.choose_action(state)
            next_state, reward, done = env.step(action)
            agent.learn(state, action, reward, next_state, done)
            state = next_state
            total_reward += reward
            if done:
                break

        agent.decay_epsilon()

        if render_demo and episode % 100 == 0:
            print(f"Episode {episode}: score={env.score} epsilon={agent.epsilon:.3f}")

    return env, agent


def watch_demo(agent, env, steps=120, delay_ms=150):
    gui = SnakeGUI(env)
    state = env.reset()
    for _ in range(steps):
        gui.draw()
        time.sleep(delay_ms / 1000)
        if env.done:
            break
        action = agent.choose_action(state, explore=False)
        next_state, reward, done = env.step(action)
        state = next_state
        if done:
            gui.draw()
            break
    gui.root.mainloop()


def main():
    print("Training the snake agent...")
    env, agent = train_agent(episodes=1200, max_steps=180)
    print(f"Training complete. Final score: {env.score}")
    print("Starting a demonstration run...")
    watch_demo(agent, env, steps=180, delay_ms=120)


if __name__ == "__main__":
    main()
