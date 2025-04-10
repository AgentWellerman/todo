from typing import Optional



class Todo():
    def __init__(self, id:int, title:str, description:Optional[str] = None, completed:bool = False):
        self.id = id
        self.title = title
        self.description = description
        self.completed = completed

    def dict(self):
        return {
            "id": self.id,
            "title": self.title, 
            "description": self.description,
            "completed": self.completed
        }

# def get_todos():
#     return[todo.dict() for todo in fake_db]

# def get_todo_by_id(todo_id: int):
#     for todo in fake_db:
#         if todo.id == todo_id:
#             return  todo_id.dict()
#     return None
    
fake_db: list[Todo] = []