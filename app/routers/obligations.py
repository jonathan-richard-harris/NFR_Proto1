from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("/", response_class=HTMLResponse)
async def obligations_page(request: Request):
    """Render a page showing the obligations selection."""
    return templates.TemplateResponse("obligations.html", {"request": request, "selected": "Obligations"})
