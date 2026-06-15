import random

def world_cup_simulation():
    # A list of top contenders for the 2026 World Cup
    contenders = ["Argentina", "France", "Brazil", "England", "Spain", "Germany", "Portugal", "Morocco"]
    
    print("Welcome to the 2026 World Cup Winner Simulator!")
    print("Available teams to check or simulate:", ", ".join(contenders))
    print("-" * 60)

    while True:
        user_input = input("\nEnter a country to simulate (or type 'exit' to quit, 'list' to see teams): ").strip()

        #exit the loop 
        if user_input.lower() == 'exit':
            print("\nExiting the simulator.")
            break

        if user_input.lower() == 'list':
            print(f"Contenders: {', '.join(contenders)}")
            pass  # Does nothing, execution moves seamlessly to the next block
            
        # checking if the entered country is in our simulator's list
    
        if user_input.lower() == 'list':
            continue

        # Format input to match title case (e.g., 'france' -> 'France')
        chosen_team = user_input.title()

        #  skip the rest of the loop if input is invalid
        if chosen_team not in contenders:
            print(f"Error: '{user_input}' is not in the simulator database. Please try a qualified team.")
            continue  # Skips the simulation below and jumps back to the top of the loop

        #  Simulation Logic 
        print(f"\nSimulating the 2026 World Cup journey for {chosen_team}...")
        
        # generate a random probability simulation
        chance = random.randint(1, 10)

        if chance >= 8:
            print(f"SUCCESS! {chosen_team} puts on a masterclass and WINS the 2026 World Cup!")
        elif chance >= 5:
            print(f"So close! {chosen_team} made it to the finals but finished as runners-up.")
        else:
            print(f"Heartbreak! {chosen_team} was knocked out in the early knockout stages.")

world_cup_simulation()