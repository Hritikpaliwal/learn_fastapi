
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
def get_item(item_id: int = Path ( description = "The ID of the item you would wana pull")):
    return inventory[item_id]

@app.get("/get-by-name")
def get_item(*, item_id: int,name: Optional[str] = None ):
    for item_id in inventory:
        if inventory[item_id]["name"] == name:
            return inventory[item_id]
    return{"Data": "Not Found"}

@app.post("/create-item")
def create_item(item_id: int,item: Item):
    if item_id in inventory:
      return {"Error": "Item already exists."}\
    
    inventory[item_id] = {"name": item.name, "brand": item.brand, "price": item.price}
    return inventory[item_id]