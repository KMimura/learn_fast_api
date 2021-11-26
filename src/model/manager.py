from model import model
from typing import List
from fastapi import HTTPException

class ItemManager():
    items: List[model.Item]
    def __init__(self):
        self.items = []

    def create(self, items: List[model.Item]):
        
        if len(self.items) > 0:
            items_sorted_by_id = sorted(self.items,key=lambda x: x.id)
            print(items_sorted_by_id)
            biggest_id = items_sorted_by_id[len(items_sorted_by_id)-1].id
            new_id = biggest_id + 1
        else:
            new_id = 0
        for i in items:
            i.id = new_id
            self.items.append(i)
            new_id += 1

    def delete(self, item_id: int, item: model.Item):
        delete_position = None
        for i, item in enumerate(self.items):
            if item['id'] == item_id:
                delete_position = i
                break
        if delete_position is not None:
            self.items = self.items.pop(delete_position)

    def read(self, item_id: int) -> model.Item:
        if item_id is not None:
            item_retrieved_arr = [i for i in self.items if i['id'] == item_id]
            if len(item_retrieved_arr) > 0:
                item_retrieved = item_retrieved_arr[0]
            else:
                item_retrieved = self.items
        else:
            item_retrieved = self.items
        return item_retrieved

    def update(self, item_id: int, item: model.Item):
        item_to_update = [i for i in self.items if i.id == item_id]
        if len(item_to_update) != 1:
            raise HTTPException(status_code=404, detail="no items found")
        # delete and add
        self.items = [i for i in self.items if i.id != item_id]
        self.items.append(item)
