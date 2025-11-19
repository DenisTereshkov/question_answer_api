from fastapi import FastAPI
from src.core.db import engine, Base
from src.api.routers import main_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(main_router)

@app.get("/")
def start_root():
    return {"API": "is running"}

app.include_router(main_router)