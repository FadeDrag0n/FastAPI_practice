import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import Field, BaseModel

app = FastAPI()

todolist = []

class ToDoCreate(BaseModel):
    name: str = Field(max_length=50)
    description: str = Field(max_length=500)

class ToDo(BaseModel):
    id: int
    name: str
    description: str

@app.post("/todos", tags=["Todos"], summary="Create New Todo")
def create_todo(to_do_create: ToDoCreate) -> dict:
    todolist.append({"id": len(todolist)+1, **to_do_create.model_dump()})
    return {"success": True}





@app.get("/todos", tags=["Todos"], summary="Get Todos", response_model=list[ToDo])
def get_todos() -> list[ToDo]:
    return todolist

@app.delete("/todos/{id_}", tags=["Todos"], summary="Remove Todo")
def remove_todo(id_: int) -> dict:
    for do in todolist:
        if do["id"] == id_:
            todolist.remove(do)
            return {"success": True}
    raise HTTPException(status_code=404, detail='Do not exist')



if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)