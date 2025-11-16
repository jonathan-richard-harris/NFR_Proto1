from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import List

app = FastAPI(title="NFR Proto1")

# Mount static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")


class Item(BaseModel):
    id: int
    name: str


# In-memory store for demo
_items: List[Item] = [Item(id=1, name="Example")]


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    """Render a simple frontend page."""
    return templates.TemplateResponse("index.html", {"request": request, "items": _items})


@app.get("/api/health")
async def health():
    return JSONResponse({"status": "ok"})


@app.get("/api/items", response_model=List[Item])
async def list_items():
    return _items


@app.post("/api/items", response_model=Item)
async def create_item(item: Item):
    _items.append(item)
    return item
