from fastapi import FastAPI

from .schema import Item
from .config import settings


app = FastAPI(
    title=settings.name,
    description="This is a very fancy project, with auto docs for the API and everything",
    version=settings.version
)


@app.get("/")
def read_root():
    return "Visit /docs for the API docs"


@app.get("/info")
async def info():
    return {"app": settings.name, "version": settings.version, "debug_mode": settings.debug_mode }


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}
