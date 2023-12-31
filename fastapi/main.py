

# from fastapi import FastAPI
# from pydantic import BaseModel, EmailStr

# app = FastAPI()


# class UserIn(BaseModel):
#     username: str
#     password: str
#     email: EmailStr
#     full_name: str | None = None


# class UserOut(BaseModel):
#     username: str
#     email: EmailStr
#     full_name: str | None = None


# class UserInDB(BaseModel):
#     username: str
#     hashed_password: str
#     email: EmailStr
#     full_name: str | None = None


# def fake_password_hasher(raw_password: str):
#     return "supersecret" + raw_password


# def fake_save_user(user_in: UserIn):
#     hashed_password = fake_password_hasher(user_in.password)
#     user_in_db = UserInDB(**user_in.dict(), hashed_password=hashed_password)
#     print("User saved! ..not really")
#     return user_in_db

# @app.post("/user/", response_model=UserOut)
# async def create_user(user_in: UserIn):
#     user_saved = fake_save_user(user_in)
#     return user_saved
# from typing import Annotated

# from fastapi import FastAPI, File, UploadFile

# app = FastAPI()


# @app.post("/files/")
# async def create_file(file: Annotated[bytes, File()]):
#     return {"file_size": len(file)}


# @app.post("/uploadfile/")
# async def create_upload_file(file: UploadFile):
#     return {"filename": file.filename}

# from typing import Annotated, Union

# from fastapi import FastAPI, File, UploadFile

# app = FastAPI()


# @app.post("/files/")
# async def create_file(file: Annotated[Union[bytes, None], File()] = None):
#     if not file:
#         return {"message": "No file sent"}
#     else:
#         return {"file_size": len(file)}


# @app.post("/uploadfile/")
# async def create_upload_file(file: Union[UploadFile, None] = None):
#     if not file:
#         return {"message": "No upload file sent"}
#     else:
#         return {"filename": file.filename}


# from typing import Annotated

# from fastapi import FastAPI, File, UploadFile

# app = FastAPI()


# @app.post("/files/")
# async def create_file(file: Annotated[bytes, File(description="A file read as bytes")]):
#     return {"file_size": len(file)}


# @app.post("/uploadfile/")
# async def create_upload_file(
#     file: Annotated[UploadFile, File(description="A file read as UploadFile")],
# ):
#     return {"filename": file.filename}

# from typing import Annotated

# from fastapi import FastAPI, File, UploadFile
# from fastapi.responses import HTMLResponse

# app = FastAPI()


# @app.post("/files/")
# async def create_files(
#     files: Annotated[list[bytes], File(description="Multiple files as bytes")],
# ):
#     return {"file_sizes": [len(file) for file in files]}


# @app.post("/uploadfiles/")
# async def create_upload_files(
#     files: Annotated[
#         list[UploadFile], File(description="Multiple files as UploadFile")
#     ],
# ):
#     return {"filenames": [file.filename for file in files]}


# @app.get("/")
# async def main():
#     content = """
# <body>
# <form action="/files/" enctype="multipart/form-data" method="post">
# <input name="files" type="file" multiple>
# <input type="submit">
# </form>
# <form action="/uploadfiles/" enctype="multipart/form-data" method="post">
# <input name="files" type="file" multiple>
# <input type="submit">
# </form>
# </body>
#     """
#     return HTMLResponse(content=content)

# from typing import Annotated

# from fastapi import FastAPI, File, Form, UploadFile

# app = FastAPI()


# @app.post("/files/")
# async def create_file(
#     file: Annotated[bytes, File()],
#     fileb: Annotated[UploadFile, File()],
#     token: Annotated[str, Form()],
# ):
#     return {
#         "file_size": len(file),
#         "token": token,
#         "fileb_content_type": fileb.content_type,
#     }

# from fastapi import FastAPI, HTTPException

# app = FastAPI()

# items = {"foo": "The Foo Wrestlers"}


# @app.get("/items-header/{item_id}")
# async def read_item_header(item_id: str):
#     if item_id not in items:
#         raise HTTPException(
#             status_code=404,
#             detail="Item not found",
#             headers={"X-Error": "There goes my error"},
#         )
#     return {"item": items[item_id]}

# from fastapi import FastAPI, HTTPException
# from fastapi.exceptions import RequestValidationError
# from fastapi.responses import PlainTextResponse
# from starlette.exceptions import HTTPException as StarletteHTTPException

# app = FastAPI()


# @app.exception_handler(StarletteHTTPException)
# async def http_exception_handler(request, exc):
#     return PlainTextResponse(str(exc.detail), status_code=exc.status_code)


# @app.exception_handler(RequestValidationError)
# async def validation_exception_handler(request, exc):
#     return PlainTextResponse(str(exc), status_code=400)


# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
#     if item_id == 3:
#         raise HTTPException(status_code=418, detail="Nope! I don't like 3.")
#     return {"item_id": item_id}

# from typing import Annotated

# from fastapi import Depends, FastAPI

# app = FastAPI()


# fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


# class CommonQueryParams:
#     def __init__(self, q: str | None = None, skip: int = 0, limit: int = 100):
#         self.q = q
#         self.skip = skip
#         self.limit = limit


# @app.get("/items/")
# async def read_items(commons: Annotated[CommonQueryParams, Depends(CommonQueryParams)]):
#     response = {}
#     if commons.q:
#         response.update({"q": commons.q})
#     items = fake_items_db[commons.skip : commons.skip + commons.limit]
#     response.update({"items": items})
#     return response
  
  









# import shutil
# import os
# from fastapi import FastAPI, File, UploadFile

# app = FastAPI()

# @app.post("/api/upload_files/")
# async def upload_file(file: UploadFile):
#     upload_dir = os.path.join(os.getcwd(), "uploads")
#     # create dir if not present
#     #upload_dir
#     if not os.path.exists(upload_dir):
#         os.makedirs(upload_dir)

#     # to get the destination path
#     dest = os.path.join(upload_dir, file.filename)
#     #print(dest)
    
#     # copy the file contents
#     with open(dest, "wb") as buffer:
#         shutil.copyfileobj(file.file, buffer)

#     return {dest}
#     # return {"filename": file.filename}

import shutil
import os
from fastapi import FastAPI, File, UploadFile,HTTPException
import zipfile
import logging
from fastapi.responses import JSONResponse
import json

app = FastAPI()

# Set up logging
logging.basicConfig(level=logging.INFO)

@app.post("/api/uploads/")
async def upload_file(file: UploadFile):
    upload_dir = os.path.join(os.getcwd(), "uploads")
    
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)

    dest = os.path.join(upload_dir, file.filename)
    logging.info("File uploaded: %s ", dest)  # Add the print statement here
    
    with open(dest, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    #to unzip the file
    with zipfile.ZipFile(dest, "r") as zip_ref:
        zip_ref.extractall(upload_dir)
        
    # return {"message":dest}
    
    #check dxf file exist or not
    dxf_file_path = os.path.join(upload_dir,"/Users/dailyAnurag/learn/fastapi/uploads/G150623161255_161255/output/G150623161255_161255.dxf")
    if not os.path.exists(dxf_file_path):
       raise HTTPException(status_code=401, detail= "dxf file not found")
    
    #read the json file
    with open("/Users/dailyAnurag/learn/fastapi/uploads/G150623161255_161255/G150623161255_161255.json") as file:
        data = json.load
        
    return data

