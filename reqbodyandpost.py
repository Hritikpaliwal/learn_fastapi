
from fastapi import FastAPI,Path
from typing import Optional
from pydantic import BaseModel

#initializes api
app  = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None

inventory = {
    1: {
        "name": "milk",
        'price': 90,
        "brand" : "Regular"
    }
}

@app.get("/get_item/{item_id}")
def get_item(item_id: int = Path (None, description = "The ID of the item you would wana pull", gt=0, lt=2)):
    return inventory[item_id]

@app.get("/get-by-name")
def get_item(name: str):
    for item_id in inventory:
        if inventory[item_id]["name"]== name:
            return inventory[item_id]
    return{"Data": "not found"}