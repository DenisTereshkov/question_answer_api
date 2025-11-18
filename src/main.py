from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def start_root():
    return {"API": "is running"}
