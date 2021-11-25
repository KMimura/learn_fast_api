from typing import Optional, List
from fastapi import FastAPI
from model import model, manager

itemManager = manager.ItemManager()
app = FastAPI()


@app.get("/items/{item_id}")
@app.get("/items")
def read_item(item_id: Optional[int]=None, q: Optional[str]=None):
    return itemManager.read(item_id)

@app.put("/items/{item_id}")
def update_item(item_id: int, item: model.Item):
    return {"item_name": item.name, "item_id": item_id}

@app.post("/items")
def create_item(items: List[model.Item]):
    itemManager.create(items)
    return {"status":"tmp"}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return itemManager.delete(item_id)