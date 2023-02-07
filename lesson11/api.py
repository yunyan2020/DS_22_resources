from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

from db import DB


class Todo(BaseModel):
    id: int = None
    title: str
    description: str


app = FastAPI()
db = DB("todo.db")
app.curr_id = 1
app.todos: List[Todo] = []


@app.get("/")
def root():
    return "Hello and welcome to Antons todos!"


@app.get("/todos")
def get_todos():
    get_todo_query = """
    SELECT * FROM todo
    """
    data = db.call_db(get_todo_query)
    print(data)
    todos = []
    for element in data:
        id,title,descrition = element
        todos.append(Todo(id=id,title=title,description=descrition ))
        pass
    return todos


@app.get("/todo/{id}")
def get_todo(id: int):
    return "Returns a single task with id " + str(id)


@app.post("/add_todo")
def add_todo(todo: Todo):
    insert_query = """
    INSERT INTO todo (title,description)
    VALUES (?,?)
    """
    # print(todo)
    # todo.id = app.curr_id
    # app.todos.append(todo)
    # app.curr_id += 1
    db.call_db(insert_query,todo.title,todo.description)
    return "Adds a task"


@app.delete("/delete_todo/{id}")
def delete_todo(id: int):
    delete_query = """
    DELETE FROM todo WHERE id = ?
    """
    db.call_db(delete_query,id)
    # app.todos = list(filter(lambda x: x.id != id, app.todos))
    return True


@app.put("/update_todo/{id}")
def update_todo(id: int, new_todo: Todo):
    update_todo_query = """
    UPDATE todo
    SET title = ? , description = ?
    WHERE id = ?
    """
    db.call_db(update_todo_query,id,new_todo.title,new_todo.description)
    # for todo in app.todos:
    #     if todo.id == id:
    #         todo.title = new_todo.title
    #         todo.description = new_todo.description
    return True
