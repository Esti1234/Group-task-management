from fastapi import FastAPI

app = FastAPI


@app.get("/tasks")
def read_root():
    return {"message": "Hello World"}
