from fastapi import FastAPI

app = FastAPI()


# 라우터 등록
#app.include_router()

@app.get("/")
async def root():
    return {"message": "Hello World"}


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

    uvicorn.run("main:app", host="localhost", port=8080, reload=True)