from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

@app.get("/")
async def root():
    return {"message": "Welcome to the Panic room!"}

@app.get("/posts")
def get_posts():
    return{'data':'Here gonna be a posts'}

@app.post('/createposts')
def create_post(post:Post):
    return {'msg':'new post was created successfully'}