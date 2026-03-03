import json
import os

# Path to the tasks.json file
DATA_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "tasks.json")


def load_tasks():
    """Load tasks from the JSON file."""
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []


def save_tasks(tasks):
    """Save tasks to the JSON file."""
    with open(DATA_FILE, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task(task_description: str):
    """Add a new task."""
    tasks = load_tasks()
    tasks.append(task_description)
    save_tasks(tasks)
    return f"Task added: {task_description}"


def show_tasks():
    """Return all tasks."""
    tasks = load_tasks()
    if not tasks:
        return "No tasks found."

    response = "Your Tasks:\n"
    for index, task in enumerate(tasks, start=1):
        response += f"{index}. {task}\n"

    return response


def delete_task(task_number: int):
    """Delete a task by its number."""
    tasks = load_tasks()

    if 1 <= task_number <= len(tasks):
        removed = tasks.pop(task_number - 1)
        save_tasks(tasks)
        return f"Deleted task: {removed}"
    else:
        return "Invalid task number."
