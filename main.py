from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from random import randrange

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None
    
    
my_posts = [{"id":1,"title": "Post 1", "content" : "Example content for post 1",}, {"id":2, "title": "Post 2", "content":"Example content for post 2"}]

def find_post(id):
    for p in my_posts:
        if p['id'] == id:
            return p

@app.get("/")
async def root():
    return {"message": "Welcome to the Panic room!"}

@app.get("/posts")
def get_posts():
    return{"data": my_posts}

@app.post("/posts")
def create_post(post:Post):
    post_dict = post.model_dump()
    post_dict['id'] = randrange(0, 10000000)

    my_posts.append(post_dict)
    return{"data": post_dict}

@app.get("/posts/{id}")
def get_post(id:int):
    post = find_post(id)
    return {"post_details": post}