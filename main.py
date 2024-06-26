from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    # extend pydantic basemodel to create Item class; initialise Item's attributes
    text: str = None
    is_done: bool = False

items = []

@app.get("/")
def root():
    return {"Hello": "World"}

@app.post("/items")
def create_item(item: Item):
    # add 'item' input to items list:
    items.append(item)
    return items

@app.get("/items")
def list_items(limit: int = 10):
    # return a list of the items; limited to the input amount or the default
    return items[0:limit]

@app.get("/items/{item_id}")
def get_item(item_id: int) -> Item:
    # retrieve an item from the list; if it does not exist then raise an error message
    if item_id < len(items):
        return items[item_id]
    else:
        raise HTTPException(status_code=404, detail=f"Item {item_id} not found")