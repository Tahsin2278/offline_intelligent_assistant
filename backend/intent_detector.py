def detect_intent(user_input: str):
    """
    Detects the user's intent based on their input.

    Parameters:
        user_input (str): The message entered by the user.

    Returns:
        tuple: A tuple containing the detected intent and related data.
    """

    # Convert input to lowercase and remove extra spaces
    user_input = user_input.lower().strip()

    # =========================
    # BASIC CONVERSATION
    # =========================

    if user_input in ["hello", "hi", "hey"]:
        return "greeting", None

    elif user_input in ["how are you", "how are you doing"]:
        return "how_are_you", None

    elif user_input in ["thank you", "thanks"]:
        return "thanks", None

    elif user_input in ["bye", "goodbye"]:
        return "bye", None

    # =========================
    # NAME MEMORY
    # =========================

    elif user_input.startswith("my name is"):
        name = user_input.replace("my name is", "").strip()
        return "save_name", name

    elif user_input in ["what is my name", "who am i"]:
        return "show_name", None

    # =========================
    # TASK MANAGEMENT
    # =========================

    elif user_input.startswith("add task"):
        task_description = user_input.replace("add task", "").strip()
        return "add_task", task_description

    elif user_input.startswith("add "):
        task_description = user_input.replace("add", "", 1).strip()
        return "add_task", task_description

    elif user_input.startswith("remember to"):
        task_description = user_input.replace("remember to", "", 1).strip()
        return "add_task", task_description

    elif user_input in ["show tasks", "list tasks", "view tasks"]:
        return "show_tasks", None

    elif user_input.startswith("delete task"):
        try:
            task_number = int(user_input.replace("delete task", "").strip())
            return "delete_task", task_number
        except ValueError:
            return "delete_task", None

    elif user_input in ["clear tasks", "delete all tasks", "clear all"]:
        return "clear_tasks", None

    # =========================
    # REMINDERS
    # =========================

    elif user_input.startswith("remind me to"):
        reminder = user_input.replace("remind me to", "").strip()
        return "add_reminder", reminder

    elif user_input in ["show reminders", "view reminders"]:
        return "show_reminders", None

    # =========================
    # CALCULATOR
    # =========================

    elif user_input.startswith("calculate"):
        expression = user_input.replace("calculate", "").strip()
        return "calculate", expression

    # =========================
    # UNKNOWN COMMAND
    # =========================

    else:
        return "unknown", None