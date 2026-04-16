from fastapi import FastAPI
from backend.logic_engine import process_input

# Create FastAPI application
app = FastAPI()


@app.get("/")
def home():
    """
    Home endpoint.
    Used to check if the API is running.
    """
    return {"message": "Assistant API is running"}


@app.get("/assistant")
def assistant(user_input: str):
    """
    Assistant endpoint.

    Receives user input from the GUI,
    sends it to the logic engine,
    and returns the response.
    """

    result = process_input(user_input)
    return {"response": result}