# Optional but professional
from backend.intent_detector import detect_intent

print(detect_intent("hello"))
print(detect_intent("my name is John"))
print(detect_intent("show tasks"))
print(detect_intent("delete task 2"))
print(detect_intent("remind me to study physics"))
print(detect_intent("calculate 5 + 10"))