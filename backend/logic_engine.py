from backend.intent_detector import detect_intent
from backend.task_manager import add_task, show_tasks, delete_task


def process_input(user_input: str):
    """
    Main controller of the assistant.
    Detects intent and executes corresponding action.
    """

    intent, data = detect_intent(user_input)

    if intent == "add_task":
        if not data:
            return "Please specify a task to add."
        return add_task(data)

    elif intent == "show_tasks":
        return show_tasks()

    elif intent == "delete_task":
        if data is None:
            return "Please specify the task number to delete."
        return delete_task(data)

    else:
        return "Sorry, I don't understand that command."