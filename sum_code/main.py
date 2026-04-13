import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/")
def root():
    return FileResponse("index.html")

@app.get("/sum")
def sum_numbers(a: float, b: float):
    return {"result": a + b}

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)