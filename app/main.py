import uvicorn

from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

if __name__ == '__main__':
    # If this is being ran directly as a script, run an internal uvicorn server
    # to service API requests
    uvicorn.run(app, host='0.0.0.0', port=8000)
