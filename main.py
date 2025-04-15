"""from fastapi  import FastAPI, HTTPException
from typing import Optional
from app.crud import create_todo, get_all_todos, get_todo_by_id, update_todo, delete_todo

app = FastAPI()

@app.post("/todos/")
def create_task(title: str, description: Optional[str] = None):
    return create_todo(title, description)

@app.get("/todos/")
def read_todos():
    return get_all_todos()

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

 

"""


"""from fastapi import FastAPI, HTTPException
from app.crud import create_todo, delete_todo, get_all_todos, get_todo_by_id, udpate_todo
from app.models import Todocreate

app = FastAPI()

@app.post("/todos/")
def create_task(todo: Todocreate):
    return create_todo(todo)

@app.get("/todos/")
def read_todos():
    return get_all_todos()
    
@app.get("/todos/{todo_id}")
def read_todo(todo_id:int):
    todo = get_todo_by_id(todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail = "item not found check your code")
    return todo

@app.put("/todos/{todo_id}")
def update_task(todo_id: int, todo_update: dict):
    success = udpate_todo(todo_id, todo_update)
    if not success:
        raise HTTPException(status_code=404, detail="item not found, check your code")
    return success

@app.delete("/todos/{todo_id}")
def delete_task(todo_id: int):
    deleted = delete_todo(todo_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Item not found, check your code")
    return deleted"""






from fastapi import FastAPI, HTTPException
from app.crud import create_todo, get_all_todos, get_todo_by_id, update_todo, delete_todo
from app.models import Todocreate


app = FastAPI()

@app.post("/todos/")
async def create_task(todo: Todocreate):
    return await create_todo(todo)

@app.get("/todos/")
async def read_todos():
    return await get_all_todos()

@app.get("/todos/{todo_id}")
async def read_todo(todo_id: str):
    todo = await get_todo_by_id(todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@app.put("/todos/{todo_id}")
async def update_task(todo_id: str, title: str = None, description: str = None, completed: bool = None):
    todo = await update_todo(todo_id, title, description, completed)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@app.delete("/todos/{todo_id}")
async def delete_task(todo_id: str):
    if not await delete_todo(todo_id):
        raise HTTPException(status_code=404, detail="Todo not found")
    return {"message": "Todo deleted"}

@app.get("/health")
async def health_check():
    return {"status": "ok"}



#commit for github 12312312
