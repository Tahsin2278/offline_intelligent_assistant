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
    Main controller of the assistant.

    This function receives user input, sends it to the intent detector,
    and then executes the correct action based on the detected intent.
    """

    # Detect the user's intent and any related data
    intent, data = detect_intent(user_input)

    # =========================
    # BASIC CONVERSATION
    # =========================

    if intent == "greeting":
        return "Hi! How can I help you today?"

    elif intent == "how_are_you":
        return "I'm doing great and ready to help!"

    elif intent == "thanks":
        return "You're welcome!"

    elif intent == "bye":
        return "Goodbye! Have a nice day!"

    # =========================
    # NAME MEMORY
    # =========================

    elif intent == "save_name":
        return save_name(data)

    elif intent == "show_name":
        return show_name()

    # =========================
    # TASK MANAGEMENT
    # =========================

    elif intent == "add_task":
        if not data:
            return "Please specify a task to add."

        return add_task(data)

    elif intent == "show_tasks":
        return show_tasks()

    elif intent == "delete_task":
        if data is None:
            return "Please specify the task number to delete."

        return delete_task(data)

    elif intent == "clear_tasks":
        return clear_tasks()

    # =========================
    # REMINDERS
    # =========================

    elif intent == "add_reminder":
        return add_reminder(data)

    elif intent == "show_reminders":
        return show_reminders()

    # =========================
    # CALCULATOR
    # =========================

    elif intent == "calculate":
        try:
            result = eval(data)
            return f"The answer is {result}"
        except:
            return "Sorry, I could not calculate that."

    # =========================
    # UNKNOWN COMMAND
    # =========================

    else:
        return "Sorry, I don't understand that command."