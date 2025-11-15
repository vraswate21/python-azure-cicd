from fastapi import FastAPI
from calculator import add

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Simple Calculator API"}

@app.get("/add")
def add_numbers(a: int, b: int):
    return {"result": add(a, b)}
