from app.models import Todo, fake_db
from typing import Optional

def create_todo(title:str, description:Optional[str] = None, completed:Optional[str] = None):
    new_id = len(fake_db) + 1
    new_todo = Todo(id=new_id, title = title, description = description)
    fake_db.append(new_todo)
    return new_todo.dict()

def get_all_todos():
    return[todo.dict()for todo in fake_db]

def get_todo_by_id(todo_id:int):
    for todo in fake_db:
        print(todo.id)
        if todo.id == int(todo_id):
            return todo
    return None

def update_todo(todo_id:int, title:Optional[str] = None, description:Optional[str] = None, completed:Optional[str] = None):
    todo = get_todo_by_id(todo_id)
    if todo:
        if title is not None:
            todo["title"] = title
        if description is not None:
            todo["description"] = description
        if completed is not None:
            todo["completed"] = completed
        return todo
    return None

def delete_todo(todo_id: int):
    global fake_db
    todo = get_todo_by_id(todo_id)
    fake_db = [todo for todo in fake_db if todo_id != fake_db]
    if todo:
        fake_db.remove(todo)
        return todo.dict()
    return None
