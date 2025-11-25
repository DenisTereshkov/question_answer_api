from fastapi import FastAPI

from src.api.routers import main_router
from src.core.db import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(main_router)


@app.get("/")
def start_root():
    return {"API": "is running"}


app.include_router(main_router)
