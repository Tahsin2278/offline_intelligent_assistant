from fastapi import FastAPI
from backend.logic_engine import process_input

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Assistant API is running"}

@app.get("/assistant")
def assistant(user_input: str):
    result = process_input(user_input)
    return {"response": result}