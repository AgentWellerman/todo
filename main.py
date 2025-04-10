from fastapi  import FastAPI, HTTPException
from typing import Optional
from app.crud import create_todo, get_all_todos, get_todo_by_id, update_todo, delete_todo

app = FastAPI()

@app.post("/todos/")
def create_task(title: str, description: Optional[str] = None):
    return create_todo(title, description)

@app.get("/todos/")
def read_todos():
    todos = get_all_todos()
    print(todos)
    return todos

@app.get("/todos/{todo_id}")
def read_todo(todo_id: int):
    todo = get_todo_by_id(todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@app.put("/todos/{todo_id}")
def update_task(todo_id: int, title: Optional[str] = None, description: Optional[str] = None, completed: Optional[bool] = None):
    todo = update_todo(todo_id, title, description, completed)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@app.delete("/todos/{todo_id}")
def delete_task(todo_id: int):
    todo = delete_todo(todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return{"message":"todo deleted succesfully"}

 

