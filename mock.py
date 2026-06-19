def generate_tasks(n=100_000, seed=42):
    random.seed(seed)
    today = datetime.now()
    tasks = []
    for i in range(n):
        name = f"Task-{i:06d}"
        priority = random.randint(1, 5)
        days_out = random.randint(0, 60)
        deadline = (today + timedelta(days=days_out)).strftime("%Y-%m-%d")
        tasks.append({"name": name, "priority": priority, "deadline": deadline})
    return tasks

def parse_task_dates(tasks):
    parsed = []
    for task in tasks:
        new_task = dict(task)
        if isinstance(new_task["deadline"], str):
            new_task["deadline"] = datetime.strptime(new_task["deadline"], "%Y-%m-%d")
        parsed.append(new_task)
    return parsed