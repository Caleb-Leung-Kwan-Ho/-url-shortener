from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from models import UrlModel, UserModel

app = FastAPI()
url_id = -1

test_table = {}

"""
class UrlModel(BaseModel):
    short_url = str
    og_url = str #og stands for orginal

class UserModel(BaseModel):
    email = str
    username = str 
    password = str
    level = int
"""


@app.get("/")
async def root():
    return {"message": "Go help yourself"}

@app.get("/list_urls")
def read_urls():
    arr = []
    return test_table
"""
    arr = []
    for url in UrlModel:
        arr.append({
            "short_url": url.short_url,
            "original_url": url.og_url
                    })
    return arr
"""

@app.get("/redirect{short_url}")
def get_url(short_url):
    if short_url in test_table:
        return {"original_url": test_table[short_url]}
    return {"error_message": "No URL found for 'nonexistent` found."}

"""
    if short_url in UrlModel:
        return {"original_url": UrlModel[short_url].og_url}
    return {"error_message": "No URL found for 'nonexistent` found."}
"""

@app.post("/shorten_url(url, short_url: optional)")
def create_url(short_url, og_url):
    if short_url in test_table:
        raise HTTPException( status_code= 404, detail= {"error_message": "Short URL" +short_url+ "already exists."})
    if not short_url:
        test_table[url_id] = og_url
        url_id += 1
        return {"short_url": "exampleShort" + str(url_id)}
    test_table[short_url] = og_url
    return {"short_url": short_url}


"""
    if short_url in UrlModel.scan():
        raise HTTPException( status_code= 404, detail= {"error_message": "Short URL" +short_url+ "already exists."})
    if not short_url:
        #perform insert opertation with url_id as key
        url_id += 1
        return {"short_url": "exampleShort" + str(url_id)}
    #perform insert opertation with short_url as key
    return {"short_url": short_url}
"""