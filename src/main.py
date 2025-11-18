from fastapi import FastAPI

from src.api.routers import main_router

app = FastAPI()


@app.get("/")
def start_root():
    return {"API": "is running"}

app.include_router(main_router)