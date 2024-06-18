from fastapi import FastAPI

app = FastAPI()

items = []

@app.get("/")
def root():
    return {"Hello": "World"}

@app.post("/items")
def create_item(item: str):
    # add 'item' input to items list:
    items.append(item)
    return item

@app.get("/items/{item_id}")
def get_item(item_id: int) -> str:
    # retrieve an item from the list
    item = items[item_id]
    return item