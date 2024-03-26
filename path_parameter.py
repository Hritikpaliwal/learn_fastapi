
#This is an example for path parameters:
#Path parameters in FastAPI are placeholders in the URL path
#that capture specific values and are defined within curly braces {} in the route definition.

from fastapi import FastAPI

#initializes api
app1 = FastAPI()

inventory = {
    1: {
        "name": "milk",
        'price': 90,
        "brand" : "Regular"
    }
}

@app1.get("/get_item/{item_id}")
def get_item(item_id: int):
    return inventory[item_id]