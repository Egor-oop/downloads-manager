from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn

from manage import manage

app = FastAPI()

origins = [
    'http://localhost:3000',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


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
