from fastapi import FastAPI, HTTPException
from pathlib import Path
import os

from fastapi.responses import FileResponse

from schemas.my_file import MyFile

app = FastAPI()

UPLOAD_DIRECTORY = Path('./files')

@app.get("/")
async def hello():
    return {"status": "ok"}

# запись
# POST /files
# with open("file", "w+") as file:
#     file.read()


@app.get("/files/{subpath:path}")
async def get_exact_file(subpath: str):
    file_path = Path(os.path.join(UPLOAD_DIRECTORY, subpath))

    if not file_path.exists():
        return HTTPException(status_code=400, detail="File does not exist")
    if file_path.is_dir():
        return HTTPException(status_code=400, detail="Not a regular file")

    return FileResponse(file_path)

@app.get("/files")
async def list_files() -> list[MyFile]:
    file_names = os.listdir(UPLOAD_DIRECTORY)
    file_names = sorted(file_names)

    my_files: list[MyFile] = []
    for file_name in file_names:
        my_file_path: Path = Path(os.path.join(UPLOAD_DIRECTORY, file_name))
        my_file_type = "directory" if my_file_path.is_dir() else "file"
        # my_var = условие ? если_да : если_нет
        # if file.is_dir():
        #     file_type = "directory"
        # else:
        #     file_type = "file"
        # my_file_type = "directory" если это директория, иначе "file"
        my_file: MyFile = MyFile(name=file_name, type=my_file_type)
        my_files.append(my_file)

    return my_files
