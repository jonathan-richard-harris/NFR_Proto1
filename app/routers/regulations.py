from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("/", response_class=HTMLResponse)
async def regulations_page(request: Request):
    """Render a page showing the regulations selection."""
    return templates.TemplateResponse("regulations.html", {"request": request, "selected": "Regulations"})


@router.get("/fragment", response_class=HTMLResponse)
async def regulations_fragment(request: Request):
    """Return the inner fragment for regulations."""
    return templates.TemplateResponse("fragments/regulations_fragment.html", {"request": request, "selected": "Regulations"})
