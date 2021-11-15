from typing import Optional
from fastapi import FastAPI
from model import model, manager

itemManager = manager.ItemManager()
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str]=None):
    return itemManager.retrieve(item_id)

@app.put("/items/{item_id}")
def update_item(item_id: int, item: model.Item):
    return {"item_name": item.name, "item_id": item_id}

@app.post("/items")
def create_item(item: model.Item):
    itemManager.add(item)
    return {"status":"tmp"}
