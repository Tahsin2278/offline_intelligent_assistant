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

print(add_task("Buy milk"))
print(add_task("Finish capstone"))
print(show_tasks())

print(delete_task(1))
print(show_tasks())

print(clear_tasks())
print(show_tasks())

print(save_name("John"))
print(show_name())

print(add_reminder("Study physics"))
print(add_reminder("Call mom"))
print(show_reminders())