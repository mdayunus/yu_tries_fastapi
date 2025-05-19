from fastapi import FastAPI
import json


def load_data():
    with open(r'C:\Users\dell\Documents\yu_tries_fastapi\data\users.json') as json_file:
        data = json.load(json_file)
        return data


app = FastAPI()

@app.get("/")
def hello():
    return {'meesage': 'hello \n world'}


@app.get("/about")
def about():
    return {"about": "yunus is an ai engineer aspirant"}

@app.get("/salary")
def salary():
    return {'salary': 100000}

@app.get("/users")
def users():
    data = load_data()
    return data