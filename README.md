# NFR Proto1 — FastAPI scaffold

This repository contains a minimal FastAPI backend that serves a small frontend using Jinja2 templates and static files.

Quick start (Windows PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open http://127.0.0.1:8000 in your browser.

Files created:
- `app/main.py` — FastAPI app, mounts static and templates
- `app/templates/index.html` — simple frontend
- `app/static/style.css` — CSS

Next steps:
- Add APIs and models according to your spec
- If you prefer a React/Vue frontend, I can scaffold that instead and connect it to the API
