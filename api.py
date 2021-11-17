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
        if len(self.item) > 0:
            items_sorted_by_id = self.items.sort(key=lambda x: x.id, reverse=True)
            biggest_id = items_sorted_by_id[len(items_sorted_by_id)-1]
            item.id = biggest_id + 1
        else:
            item.id = 0
        self.items.append(item)

    def delete(self, item_id: int, item: Item):
        delete_position = None
        for i, item in enumerate(self.items):
            if item['id'] == item_id:
                delete_position = i
                break
        if delete_position is not None:
            self.items = self.items.pop(delete_position)
        # self.items = [i if i['id'] != item_id else item for i in self.items]

    def retrieve(self, item_id: int) -> Item:
        if item_id is not None:
            item_retrieved_arr = [i for i in self.items if i['id'] == item_id ]
            if len(item_retrieved_arr) > 0:
                item_retrieved = item_retrieved_arr[0]
            else:
                item_retrieved = self.items
        else:
            item_retrieved = self.items
        return item_retrieved


itemManager = ItemManager()
app = FastAPI()


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

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return itemManager.delete(item_id)