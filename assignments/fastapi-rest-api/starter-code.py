"""
Starter code para o assignment 'APIs REST com FastAPI'.

Execute localmente com:
  pip install -r requirements.txt
  uvicorn starter-code:app --reload --port 8000

Visite: http://127.0.0.1:8000/docs
"""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, Dict

app = FastAPI(title="FastAPI - Assignment Starter")


class ItemBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float


class Item(ItemBase):
    id: int


db: Dict[int, Item] = {}
next_id = 1


@app.post("/items", status_code=201, response_model=Item)
def create_item(item: ItemBase):
    global next_id
    created = Item(id=next_id, **item.dict())
    db[next_id] = created
    next_id += 1
    return created


@app.get("/items", response_model=list[Item])
def list_items():
    return list(db.values())


@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    if item_id not in db:
        raise HTTPException(status_code=404, detail="Item not found")
    return db[item_id]


@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: ItemBase):
    if item_id not in db:
        raise HTTPException(status_code=404, detail="Item not found")
    updated = Item(id=item_id, **item.dict())
    db[item_id] = updated
    return updated


@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    if item_id not in db:
        raise HTTPException(status_code=404, detail="Item not found")
    del db[item_id]
    return None
