# Offline Intelligent Assistant
A logic-based offline AI assistant built using Python. This project demonstrates intent detection, modular backend architecture, API communication and a graphical user interface.

# Project Objective
The goal of this capstone project is to build a mini AI assistant that works completely offline.
The assistant detects user intent using rule-based logic and responds by executing structured tasks such as task management and basic calculations. 

# Features 
* Rule-based intent detection
* Task management (add, view, delete tasks, greetings, calculate, reminder)
* Local data storage using JSON
* FastAPI backend API
* Tkinter GUI interface
* Offline functionality (no external APIs)

# Tech Stack
* Python
* FastAPI
* Tkinter
* JSON (local storage)

# Project Structure
* backend/ - Core logic and API
* frontend/ - GUI application
* data/ - Local JSON storage
* tests/ - Unit tests

# Current status
* Project status complete for now. Will update more later.

# How to run the project
1. Open the project folder in terminal(VS code, Pycharm, Command prompt)
2. Install the required libraries :
  pip install fastapi uvicorn requests
3. Start the backend server:
  uvicorn backend.api:app --reload
4. Wait until the terminal shows:
  Application startup complete
  Uvicorn running on http://127.0.0.1:8000
5. Open a new terminal window.
6. Run the GUI file:
  python gui.py
7. The assistant window will open.
8. Enter commands such as:
 add task buy milk
 show tasks
 delete task 1
 remind me to study physics
 my name is tahsin. what is my name?
 calculate 2 + 2
 hi, hello, how are you

# Important Note
* The backend server must be running before opening the GUI. Backend and GUI must be running in seperate terminals.








