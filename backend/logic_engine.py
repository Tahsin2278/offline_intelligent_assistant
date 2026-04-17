import math
from backend.intent_detector import detect_intent
from backend.task_manager import (
    add_task,
    show_tasks,
    delete_task,
    clear_tasks,
    save_name,
    show_name,
    add_reminder,
    show_reminders
)


def process_input(user_input: str):
    """
    Main controller: Receives intent and executes the correct backend function.
    """

    # Detect the user's intent and any related data
    intent, data = detect_intent(user_input)

    # --- BASIC CONVERSATION ---
    if intent == "greeting":
        return "Hi! How can I help you today?"

    elif intent == "how_are_you":
        return "I'm doing great and ready to help!"

    elif intent == "thanks":
        return "You're welcome!"
    elif intent == "bye":
        return "Goodbye! Have a nice day!"

    # --- NAME MEMORY ---
    elif intent == "save_name":
        if not data:
            return "Please tell me your name (e.g., 'My name is John')."
        return save_name(data)

    elif intent == "show_name":
        return show_name()

    # --- TASK MANAGEMENT ---
    elif intent == "add_task":
        if not data:
            return "Please specify a task to add."

        return add_task(data)

    elif intent == "show_tasks":
        return show_tasks()

    elif intent == "delete_task":
        if data is None:
            return "Please specify a valid task number to delete."
        return delete_task(data)

    elif intent == "clear_tasks":
        return clear_tasks()

    # --------- 
    # REMINDERS 
    # ---------
    elif intent == "add_reminder":
        if not data:
            return "What would you like me to remind you about?"
        return add_reminder(data)

    elif intent == "show_reminders":
        return show_reminders()

    # ------------------------------------ 
    # CALCULATOR (Security Hardened + SQRT) 
    # ------------------------------------
    elif intent == "calculate":
        if not data:
            return "Please provide a math problem."
        
        try:
            # Whitelist: Only allow numbers, math operators, and the word 'sqrt'
            allowed_chars = "0123456789+-*/(). sqrt"
            if all(char in allowed_chars for char in data):
                # We pass math.sqrt to eval, but block all other built-ins for safety
                result = eval(data, {"__builtins__": {}, "sqrt": math.sqrt})
                return f"The answer is {result}"
            else:
                return "For security, I can only use numbers, operators, and 'sqrt'."
        except Exception:
            return "Sorry, I could not calculate that. Try: sqrt(16) or 5 * 5"

    # --------------
    # UNKNOWN COMMAND 
    # --------------
    else:
        return "Sorry, I don't understand that command. Try asking me to add a task or do some math!"