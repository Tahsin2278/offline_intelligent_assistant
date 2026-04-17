from fastapi import FastAPI, Query
from backend.logic_engine import process_input
from backend.task_manager import get_stored_name 

# Create FastAPI application
app = FastAPI(title="Offline Assistant API", version="1.0")


@app.get("/")
def home():
    """
    Home endpoint.
    Checks if a user name is saved in memory and returns a 
    personalized greeting to the GUI.
    """
    name = get_stored_name()
    if name:
        return {"status": "online", "message": f"Welcome back, {name}!"}
    
    return {"status": "online", "message": "Assistant API is running. How can I help you?"}


@app.get("/assistant")
def assistant(user_input: str = Query(None, min_length=1)):
    """
    Assistant endpoint.
    Receives user input from the GUI, sends it to the logic engine,
    and returns the JSON response.
    """
    
    # Check if input is empty or just spaces
    if not user_input or user_input.strip() == "":
        return {"response": "I didn't receive any input. Please say something!"}

    try:
        # Pass the input to the logic engine
        result = process_input(user_input)
        return {"response": result}
    except Exception as e:
        # Catch-all error handling so the API doesn't crash completely
        return {"response": f"Internal API Error: {str(e)}"}