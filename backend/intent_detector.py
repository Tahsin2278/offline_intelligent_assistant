def detect_intent(user_input: str):
    """
    Detect user intent and extract necessary data.
    Returns: (intent, data)
    """

    user_input = user_input.lower().strip()

    # ADD TASK
    if user_input.startswith("add task"):
        task_description = user_input.replace("add task", "").strip()
        return "add_task", task_description

    # SHOW TASKS
    elif user_input in ["show tasks", "list tasks", "view tasks"]:
        return "show_tasks", None

    # DELETE TASK
    elif user_input.startswith("delete task"):
        try:
            task_number = int(user_input.replace("delete task", "").strip())
            return "delete_task", task_number
        except ValueError:
            return "delete_task", None

    else:
        return "unknown", None