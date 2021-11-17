from model import model

class ItemManager():
    def __init__(self):
        self.items = []

    def add(self, item: model.Item):
        print(self.items)
        if len(self.items) > 0:
            items_sorted_by_id = sorted(self.items,key=lambda x: x.id)
            print(items_sorted_by_id)
            biggest_id = items_sorted_by_id[len(items_sorted_by_id)-1].id
            item.id = biggest_id + 1
        else:
            item.id = 0
        self.items.append(item)

    def delete(self, item_id: int, item: model.Item):
        delete_position = None
        for i, item in enumerate(self.items):
            if item['id'] == item_id:
                delete_position = i
                break
        if delete_position is not None:
            self.items = self.items.pop(delete_position)
        # self.items = [i if i['id'] != item_id else item for i in self.items]

    def retrieve(self, item_id: int) -> model.Item:
        if item_id is not None:
            item_retrieved_arr = [i for i in self.items if i['id'] == item_id]
            if len(item_retrieved_arr) > 0:
                item_retrieved = item_retrieved_arr[0]
            else:
                item_retrieved = self.items
        else:
            item_retrieved = self.items
        return item_retrieved
