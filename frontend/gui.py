import tkinter as tk
from tkinter import messagebox
import requests

class AssistantGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Offline Personal Assistant")
        self.root.geometry("500x600")

        # --- UI LAYOUT ---
        # Chat Display
        self.chat_display = tk.Text(root, height=20, width=50, state='disabled', wrap='word')
        self.chat_display.pack(padx=10, pady=10)

        # Input Field
        self.input_field = tk.Entry(root, width=40)
        self.input_field.pack(padx=10, pady=5)
        self.input_field.bind("<Return>", lambda event: self.send_message()) # Press Enter to send

        # Send Button
        self.send_button = tk.Button(root, text="Send", command=self.send_message, bg="#4CAF50", fg="white")
        self.send_button.pack(pady=10)

        # --- DYNAMIC GREETING ---
        # This calls the home endpoint to see if a name is already saved
        try:
            # We call the base URL "/" to get the status and the name-based message
            response = requests.get("http://127.0.0.1:8000/", timeout=2)
            if response.status_code == 200:
                welcome_msg = response.json().get("message", "Hello! How can I help you?")
            else:
                welcome_msg = "Hello! I am your offline assistant. How can I help you?"
        except:
            # Fallback if the API isn't running yet
            welcome_msg = "Hello! I am your offline assistant. How can I help you?"

        self.update_chat(f"Assistant: {welcome_msg}")

    def update_chat(self, message):
        """Helper to update the chat display safely."""
        self.chat_display.config(state='normal')
        self.chat_display.insert(tk.END, message + "\n\n")
        self.chat_display.config(state='disabled')
        self.chat_display.see(tk.END)

    def send_message(self):
        user_input = self.input_field.get().strip()
        if not user_input:
            return

        self.update_chat(f"You: {user_input}")
        self.input_field.delete(0, tk.END)

        # --- API CALL ---
        try:
            response = requests.get(f"http://127.0.0.1:8000/assistant", params={"user_input": user_input}, timeout=5)
            
            if response.status_code == 200:
                bot_response = response.json().get("response", "Error: No response from engine.")
                self.update_chat(f"Assistant: {bot_response}")
            else:
                self.update_chat("Assistant: Error - API returned an error.")
        
        except requests.exceptions.ConnectionError:
            self.update_chat("Assistant: [ERROR] Cannot connect to the API. Did you start uvicorn?")
            messagebox.showerror("Connection Error", "Please start the backend (uvicorn) before using the GUI.")
        except Exception as e:
            self.update_chat(f"Assistant: [ERROR] {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = AssistantGUI(root)
    root.mainloop()