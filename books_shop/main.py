import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

books = [
    {
        "id": 1,
        "title": "Book 1",
        "author": "William",
    },
    {
        "id": 2,
        "title": "Book 2",
        "author": "Artem",
    }]


@app.get(
    "/books",
    tags=["Books"],
    summary="Get all books",)
def read_books():
    return books


@app.get(
    "/books/{book_id}",
    tags=["Books"],
    summary="Get a book",)
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

class NewBook(BaseModel):
    title: str
    author: str


@app.post("/books", tags=["Books"])
def create_book(new_book: NewBook):
    books.append(
        {
            "id": len(books) + 1,
            "title": new_book.title,
            "author": new_book.author,
        }
    )
    return {"success": True, "message": "Book created successfully!"}

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)