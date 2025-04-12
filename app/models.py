from typing import Optional
from pydantic import BaseModel



class Todocreate(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False


class TodoDB(Todocreate):
    id: str

# def get_todos():
#     return[todo.dict() for todo in fake_db]

# def get_todo_by_id(todo_id: int):
#     for todo in fake_db:
#         if todo.id == todo_id:
#             return  todo_id.dict()
#     return None
    

#commit dlya proekta12313
