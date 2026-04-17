import re

def detect_intent(user_input):
    """
    Analyzes user input to determine intent and extract relevant data.
    """

    # Convert input to lowercase and remove extra spaces
    user_input = user_input.lower().strip()

    # ------------------
    # BASIC CONVERSATION 
    # ------------------
    if user_input in ["hi", "hello", "hey", "hola"]:
        return "greeting", None
    if "how are you" in user_input:
        return "how_are_you", None
    if user_input in ["thanks", "thank you"]:
        return "thanks", None
    if user_input in ["bye", "goodbye", "exit"]:
        return "bye", None

    # ----------- 
    # NAME MEMORY 
    # -----------
    if "my name is" in user_input:
        name = user_input.split("my name is")[-1].strip()
        return "save_name", name
    if "what is my name" in user_input:
        return "show_name", None

    # --------------- 
    # TASK MANAGEMENT 
    # ---------------
    if "add task" in user_input:
        task = user_input.split("add task")[-1].strip()
        return "add_task", task
    if "show tasks" in user_input or "view tasks" in user_input:
        return "show_tasks", None
    if "delete task" in user_input:
        try:
            # Extract the number from the string
            number = int(re.search(r'\d+', user_input).group())
            return "delete_task", number
        except (AttributeError, ValueError):
            return "delete_task", None
    if "clear tasks" in user_input:
        return "clear_tasks", None

    # --------- 
    # REMINDERS 
    # ---------
    if "remind me to" in user_input:
        reminder = user_input.split("remind me to")[-1].strip()
        return "add_reminder", reminder
    if "show reminders" in user_input:
        return "show_reminders", None

    # -------------------------- 
    # CALCULATOR (Including sqrt) 
    # --------------------------
    # Triggered by 'calculate' or math keywords like 'sqrt'
    if "calculate" in user_input or "sqrt" in user_input:
        expression = user_input.replace("calculate", "").strip()
        return "calculate", expression

    return "unknown", None