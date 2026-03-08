import tkinter as tk
import requests

API_URL = "http://127.0.0.1:8000/ask"


def send_message():
    user_input = user_entry.get().strip()

    if user_input == "":
        return

    # show user message
    chat_area.insert(tk.END, f"You: {user_input}\n")

    try:
        response = requests.post(API_URL, json={"question": user_input})
        data = response.json()

        answer = data.get("answer", "No response from assistant.")
        chat_area.insert(tk.END, f"Assistant: {answer}\n\n")

    except Exception:
        chat_area.insert(tk.END, "Assistant: Error connecting to backend.\n\n")

    user_entry.delete(0, tk.END)


# Main window
root = tk.Tk()
root.title("Offline Intelligent Assistant")
root.geometry("500x500")

# Chat display area
chat_area = tk.Text(root, wrap=tk.WORD, height=20, width=60)
chat_area.pack(padx=10, pady=10)

# Input frame
input_frame = tk.Frame(root)
input_frame.pack(pady=5)

# Entry field
user_entry = tk.Entry(input_frame, width=40)
user_entry.pack(side=tk.LEFT, padx=5)

# Send button
send_button = tk.Button(input_frame, text="Send", command=send_message)
send_button.pack(side=tk.LEFT)

# Allow Enter key to send message
root.bind('<Return>', lambda event: send_message())

root.mainloop()
