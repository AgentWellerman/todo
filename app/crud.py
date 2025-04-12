"""from app.models import Todo, fake_db
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
"""


from app.database import client, database, todo_collection
from app.models import Todocreate, TodoDB 
from bson import ObjectId


async def create_todo(todo:Todocreate):
    new_todo = todo.dict()
    result = await todo_collection.insert_one(new_todo)
    created_todo = await todo_collection.find_one({"_id": result.inserted_id})

    created_todo["_id"] = str(created_todo["_id"])
    return created_todo
    


async def get_all_todos():
    todos = []
    async for todo in todo_collection.find():
        todo["_id"] = str(todo["_id"])  # преобразуем ObjectId -> str
        todos.append(todo)
    return todos

"""async def get_all_todos():
    todos = await todo_collection.find().to_list(100)
    return[{**todo, "id":str(todo["_id"])} for todo in todos]"""


"""async def get_todo_by_id(todo_id: str):
    todo = await todo_collection.find_one({"_id": ObjectId})
    if todo:
        return{**todo, "id": str(todo[id])}
    return None"""

"""async def udpate_todo(todo_id: str, todo_update: dict):
    result = await todo_collection.update_one(
        {"_id":ObjectId(todo_id)}, {"$set": todo_update}
    )
    return result.modified_count > 0"""



async def get_todo_by_id(todo_id: str):
    try:
        obj_id = ObjectId(todo_id)  # преобразуем строку в ObjectId
    except Exception as e:
        print(f"Ошибка преобразования ObjectId: {e}")
        return None

    todo = await todo_collection.find_one({"_id": obj_id})
    if todo:
        todo["_id"] = str(todo["_id"])  # преобразуем обратно в str для ответа
    return todo



async def update_todo(todo_id: str, title: str = None, description: str = None, completed: bool = None):
    update_fields = {}
    if title is not None:
        update_fields["title"] = title
    if description is not None:
        update_fields["description"] = description
    if completed is not None:
        update_fields["completed"] = completed

    if update_fields:
        await todo_collection.update_one({"_id": ObjectId(todo_id)}, {"$set": update_fields})

    return await get_todo_by_id(todo_id)



async def delete_todo(todo_id:str):
        result = await todo_collection.delete_one({"_id": ObjectId(todo_id)})
        return result.deleted_count > 0



#dergy