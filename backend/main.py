from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

from manage import manage

app = FastAPI()


class Folder(BaseModel):
    path: str


@app.get("/")
async def root():
    return {"Hello": "World"}


@app.post('/manage')
async def manage_downloads(folders: list[Folder]):
    try:
        manage(folders[0].path, folders[1].path)
    except IndexError:
        raise HTTPException(status_code=400, detail="Invalid arguments")
    return {'folders': folders}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
