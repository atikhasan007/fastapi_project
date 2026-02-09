from fastapi import FastAPI, status
from pydantic import BaseModel
from typing import List
from fastapi.exceptions import HTTPException


app = FastAPI()

books = [
    {
        "id": 1,
        "title": "Think Python",
        "author": "Allen B. Downey",
        "publisher": "O'Reilly Media",
        "published_date": "2001-01-01",
        "page_content": 1234,
        "language": "English"
    },
    {
        "id": 2,
        "title": "Clean Code",
        "author": "Robert C. Martin",
        "publisher": "Prentice Hall",
        "published_date": "2008-08-01",
        "page_content": 464,
        "language": "English"
    },
    {
        "id": 3,
        "title": "Fluent Python",
        "author": "Luciano Ramalho",
        "publisher": "O'Reilly Media",
        "published_date": "2015-07-30",
        "page_content": 792,
        "language": "English"
    },
    {
        "id": 4,
        "title": "Python Crash Course",
        "author": "Eric Matthes",
        "publisher": "No Starch Press",
        "published_date": "2019-05-03",
        "page_content": 544,
        "language": "English"
    },
    {
        "id": 5,
        "title": "Automate the Boring Stuff",
        "author": "Al Sweigart",
        "publisher": "No Starch Press",
        "published_date": "2020-04-14",
        "page_content": 592,
        "language": "English"
    },
    {
        "id": 6,
        "title": "Deep Learning",
        "author": "Ian Goodfellow",
        "publisher": "MIT Press",
        "published_date": "2016-11-18",
        "page_content": 800,
        "language": "English"
    },
    {
        "id": 7,
        "title": "Hands-On Machine Learning",
        "author": "Aurélien Géron",
        "publisher": "O'Reilly Media",
        "published_date": "2022-04-12",
        "page_content": 856,
        "language": "English"
    },
    {
        "id": 8,
        "title": "Design Patterns",
        "author": "Erich Gamma",
        "publisher": "Addison-Wesley",
        "published_date": "1994-10-31",
        "page_content": 395,
        "language": "English"
    },
    {
        "id": 9,
        "title": "Introduction to Algorithms",
        "author": "Thomas H. Cormen",
        "publisher": "MIT Press",
        "published_date": "2009-07-31",
        "page_content": 1312,
        "language": "English"
    },
    {
        "id": 10,
        "title": "You Don't Know JS",
        "author": "Kyle Simpson",
        "publisher": "O'Reilly Media",
        "published_date": "2015-12-27",
        "page_content": 278,
        "language": "English"
    }
]


class Book(BaseModel):
    id: int
    title: str
    author: str
    publisher:str
    published_date:str
    page_content:int
    language:str


class BookUpdateModel(BaseModel):
    title: str
    author: str
    publisher:str
    page_content:int
    language:str



@app.get('/books', response_model=List[Book])
async def get_all_books():
    return books
    

@app.post('/books', status_code=status.HTTP_201_CREATED)
async def create_a_book(book_data: Book)->dict:
    new_book = book_data.model_dump()
    books.append(new_book)
    return new_book 



@app.get('/book/{book_id}')
async def get_book(book_id:int) -> dict:
    for book in books:
        if book['id'] == book_id:
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Book not found")




@app.patch('/book/{book_id}')
async def update_book(book_id:int , book_update_data:BookUpdateModel) -> dict:
    for book in books:
        if book['id'] == book_id:
            book['title'] = book_update_data.title
            book['author'] = book_update_data.author
            book['publisher'] = book_update_data.publisher
            book['page_content'] = book_update_data.page_content
            book['language'] = book_update_data.language

            return book

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Book not found")



@app.delete('/book/{book_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id:int):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)

            return {}
        

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Book not found")




