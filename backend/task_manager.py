import json
import os

# Create the data directory automatically if it's missing
if not os.path.exists("data"):
    os.makedirs("data")

# File paths
TASKS_FILE = "data/tasks.json"
MEMORY_FILE = "data/memory.json"
REMINDER_FILE = "data/reminders.json"

# --- HELPER FUNCTIONS ---
def load_data(file_path, default_type=list):
    """Safely loads JSON data. Returns empty list or dict if file is missing/corrupt."""
    try:
        if not os.path.exists(file_path):
            return default_type()
        with open(file_path, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return default_type()

def save_data(file_path, data):
    """Saves data to a JSON file."""
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

# --- TASK FUNCTIONS ---
def add_task(task_description):
    tasks = load_data(TASKS_FILE)
    tasks.append(task_description)
    save_data(TASKS_FILE, tasks)
    return f"Task added: {task_description}"

def show_tasks():
    tasks = load_data(TASKS_FILE)
    if not tasks:
        return "Your task list is empty."
    
    result = "Your Tasks:\n"
    for i, task in enumerate(tasks, start=1):
        result += f"{i}. {task}\n"
    return result


def delete_task(task_number):
    tasks = load_data(TASKS_FILE)
    try:
        if 1 <= task_number <= len(tasks):
            removed = tasks.pop(task_number - 1)
            save_data(TASKS_FILE, tasks)
            return f"Deleted task: {removed}"
        else:
            return "Invalid task number."
    except (ValueError, TypeError):
        return "Please provide a valid number."

def clear_tasks():
    save_data(TASKS_FILE, [])
    return "All tasks have been cleared."

# --- NAME/MEMORY FUNCTIONS ---
def save_name(name):
    memory = load_data(MEMORY_FILE, default_type=dict)
    memory["name"] = name
    save_data(MEMORY_FILE, memory)
    return f"Nice to meet you, {name}! I'll remember that."

def get_stored_name():
    memory = load_data(MEMORY_FILE, default_type=dict)
    return memory.get("name")

def show_name():
    memory = load_data(MEMORY_FILE, default_type=dict)
    name = memory.get("name")
    if name:
        return f"Your name is {name}."
    return "I don't know your name yet. You can tell me by saying 'My name is...'"

# --- REMINDER FUNCTIONS ---
def add_reminder(text):
    reminders = load_data(REMINDER_FILE)
    reminders.append(text)
    save_data(REMINDER_FILE, reminders)
    return f"Reminder set: {text}"

def show_reminders():
    reminders = load_data(REMINDER_FILE)
    if not reminders:
        return "You have no reminders."
    
    result = "Your Reminders:\n"
    for i, rem in enumerate(reminders, start=1):
        result += f"{i}. {rem}\n"
    return result