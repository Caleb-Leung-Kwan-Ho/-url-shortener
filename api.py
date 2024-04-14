from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
url_id = -1

class UrlModel(BaseModel):
    short_url = str
    og_url = str #og stands for orginal

class UserModel(BaseModel):
    email = str
    username = str 
    password = str
    level = int


@app.get("/")
async def root():
    return {"message": "Go help yourself"}

@app.get("/list_urls")
def read_urls():
    arr = []
    for url in UrlModel:
        arr.append({
            "short_url": url.short_url,
            "original_url": url.og_url
                    })
    return arr

@app.get("/redirect{short_url}")
def get_url(short_url):
    if short_url in UrlModel:
        return {"original_url": UrlModel[short_url].og_url}
    return {"error_message": "No URL found for 'nonexistent` found."}

@app.post("/shorten_url(url, short_url: optional)")
def create_url(short_url, og_url):
    if short_url in UrlModel:
        raise HTTPException( status_code= 404, detail= {"error_message": "Short URL" +short_url+ "already exists."})
    if not short_url:
        url_id += 1
        return {"short_url": "exampleShort" + str(url_id)}
    return {"short_url": short_url}
