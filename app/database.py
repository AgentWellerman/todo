from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URL= "mongodb://mongo:27017/"
DB_NAME = "todo_db"



client = AsyncIOMotorClient(MONGO_URL)
database = client[DB_NAME]
todo_collection = database.get_collection("todos")



#commit for gityhub


#azazazqa