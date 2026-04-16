import json

# File paths
TASKS_FILE = "data/tasks.json"
MEMORY_FILE = "data/memory.json"
REMINDER_FILE = "data/reminders.json"


# =========================
# TASK FUNCTIONS
# =========================

def load_tasks():
    """
    Load tasks from tasks.json.
    """
    try:
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    except:
        return []


def save_tasks(tasks):
    """
    Save tasks to tasks.json.
    """
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task(task):
    """
    Add a new task.
    """
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)

    return f"Task added successfully: {task}"


def show_tasks():
    """
    Show all saved tasks.
    """
    tasks = load_tasks()

    if not tasks:
        return "No tasks available."

    result = "Your tasks:\n"

    for index, task in enumerate(tasks, start=1):
        result += f"{index}. {task}\n"

    return result


def delete_task(task_number):
    """
    Delete a task using its number.
    """
    tasks = load_tasks()

    if task_number < 1 or task_number > len(tasks):
        return "Invalid task number."

    removed_task = tasks.pop(task_number - 1)
    save_tasks(tasks)

    return f"Task deleted successfully: {removed_task}"


def clear_tasks():
    """
    Delete all tasks.
    """
    save_tasks([])
    return "All tasks deleted successfully."


# =========================
# NAME MEMORY FUNCTIONS
# =========================

def save_name(name):
    """
    Save the user's name.
    """
    data = {"name": name}

    with open(MEMORY_FILE, "w") as file:
        json.dump(data, file, indent=4)

    return f"Nice to meet you, {name}!"


def show_name():
    """
    Show the saved user name.
    """
    try:
        with open(MEMORY_FILE, "r") as file:
            data = json.load(file)
            return f"Your name is {data['name']}"
    except:
        return "I don't know your name yet."


# =========================
# REMINDER FUNCTIONS
# =========================

def load_reminders():
    """
    Load reminders from reminders.json.
    """
    try:
        with open(REMINDER_FILE, "r") as file:
            return json.load(file)
    except:
        return []


def save_reminders(reminders):
    """
    Save reminders to reminders.json.
    """
    with open(REMINDER_FILE, "w") as file:
        json.dump(reminders, file, indent=4)


def add_reminder(reminder):
    """
    Add a reminder.
    """
    reminders = load_reminders()
    reminders.append(reminder)
    save_reminders(reminders)

    return f"Reminder saved: {reminder}"


def show_reminders():
    """
    Show all saved reminders.
    """
    reminders = load_reminders()

    if not reminders:
        return "No reminders saved."

    result = "Your reminders:\n"

    for index, reminder in enumerate(reminders, start=1):
        result += f"{index}. {reminder}\n"

    return result