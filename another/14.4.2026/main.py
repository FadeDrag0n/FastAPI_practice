import uvicorn
from fastapi import FastAPI, HTTPException

app = FastAPI()

todolist = []

@app.post("/todos", tags=["Todos"], summary="Create New Todo")
def create_todo(name: str, description: str) -> dict:
    todolist.append({"id": len(todolist)+1, "name": name, "description": description})
    return {"success": True}





@app.get("/todos", tags=["Todos"], summary="Get Todos")
def get_todos() -> list[dict]:
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