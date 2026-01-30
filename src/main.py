from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from jinja2 import Template

app = FastAPI()

# Template
templates = Jinja2Templates(directory="template")

# 라우터 등록
#app.include_router()

@app.get("/", response_class=HTMLResponse)
def serve_index(request: Request):
    model_data = {
        "title": "FastAPI Jinja2 Template Example",
        "items": ["Item 1", "Item 2", "Item 3"]
    }
    return templates.TemplateResponse("index.html", {"request": request, "model": model_data})


@app.get('/env', summary='App 환경 설정 확인', include_in_schema=False)
def root():
    from shared.config import settings
    env = {
        'APP_ENV': settings.APP_ENV,
        'DB_USER': settings.DB_USER,
        #'DB_PASSWORD': settings.DB_PASSWORD,
        'DB_HOST': settings.DB_HOST,
        'DB_PORT': settings.DB_PORT,
        'DB_DATABASE': settings.DB_DATABASE,
    }
    
    return env

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8080,
        reload=False,   # 중요
    )