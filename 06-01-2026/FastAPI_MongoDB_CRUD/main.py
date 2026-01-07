from fastapi import APIRouter, FastAPI, HTTPException
from configurations import collection
from database.schemas import all_tasks
from database.models import ToDo


app = FastAPI()
router=APIRouter()

@router.get("/")
async def get_all_todos():
    data = collection.find()
    return all_tasks(data)

@router.post("/")
async def create_task(new_task:ToDo):
    try:
        resp = collection.insert_one(dict(new_task))
        return {"status_code":200,"id": str(resp.inserted_id)}
    except Exception as e:
        return HTTPException(status_code = 500, detail=f"Some error occured {e}")   
     

    


app.include_router(router)


