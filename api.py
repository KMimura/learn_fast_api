from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None
    id: Optional[int] = None

class ItemManager():
    def __init__(self):
        self.items = []

    def add(self, item: Item):
        if len(self.items) > 0:
            items_sorted_by_id = self.items.sort(key=lambda x: x.id, reverse=True)
            biggest_id = items_sorted_by_id[len(items_sorted_by_id)-1]
            item.id = biggest_id + 1
        else:
            item.id = 0
        self.items.append(item)

    def delete(self, item_id: int, item: Item):
        self.items = [i if i['id'] != item_id else item for i in self.items]

    def retrieve(self, item_id: int) -> Item:
        if item_id is not None:
            try:
                item_retrieved = [i for i in self.items if i['id'] == item_id ][0]
            except IndexError:
                item_retrieved = []
        else:
            item_retrieved = self.items
        return item_retrieved


itemManager = ItemManager()
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str]=None):
    return itemManager.retrieve(item_id)

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

@app.post("/items")
def create_item(item: Item):
    itemManager.add(item)
    return {"status":"tmp"}
