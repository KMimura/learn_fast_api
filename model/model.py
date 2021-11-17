from pydantic import BaseModel
from typing import Optional


class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None

class Item_with_id(Item):
    id: int