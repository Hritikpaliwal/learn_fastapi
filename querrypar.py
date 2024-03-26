
from fastapi import FastAPI,Path
from typing import Optional
from pydantic import BaseModel

#initializes api
app  = FastAPI()

inventory = {
    1: {
        "name": "milk",
        'price': 90,
        "brand" : "Regular"
    }
}

@app.get("/get_item/{item_id}")
def get_item(item_id: int = Path ( description = "The ID of the item you would wana pull", gt=0, lt=2)):
    return inventory[item_id]

@app.get("/get-by-name")
def get_item(*, item_id: int,name: Optional[str] = None, test: int):
    for item_id in inventory:
        if inventory[item_id]["name"] == name:
            return inventory[item_id]
    return{"Data": "Not Found"}