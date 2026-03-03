def detect_intent(user_input: str) -> str:
    """
    Detects user intent based on simple rule-based keyword matching.
    Returns a string representing the detected intent.
    """

    user_input = user_input.lower().strip()

    if any(word in user_input for word in ["add task", "create task", "new task"]):
        return "add_task"

    elif any(word in user_input for word in ["show tasks", "list tasks", "view tasks"]):
        return "show_tasks"

    elif any(word in user_input for word in ["delete task", "remove task"]):
        return "delete_task"

    elif any(op in user_input for op in ["+", "-", "*", "/"]):
        return "calculate"

    elif any(word in user_input for word in ["hello", "hi", "hey"]):
        return "greeting"

    else:
        return "unknown"
    