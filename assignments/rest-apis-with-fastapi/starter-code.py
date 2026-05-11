from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class ItemCreate(BaseModel):
    name: str
    description: str


items = [
    {"id": 1, "name": "Notebook", "description": "A paper notebook for class notes."},
    {"id": 2, "name": "Keyboard", "description": "A mechanical keyboard for coding."},
]


@app.get("/")
def read_root():
    return {"message": "Update this API to complete the assignment."}


@app.get("/items")
def get_items():
    return items


@app.get("/items/{item_id}")
def get_item(item_id: int):
    for item in items:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")


@app.post("/items")
def create_item(item: ItemCreate):
    new_item = {
        "id": len(items) + 1,
        "name": item.name,
        "description": item.description,
    }
    items.append(new_item)
    return new_item