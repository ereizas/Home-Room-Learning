from fastapi import FastAPI, File, UploadFile
from fastapi.exceptions import HTTPException
import json

app = FastAPI()

#request for uploading the images
@app.post("/upload_images/")
async def upload_image(file: UploadFile):
    if file.content_type!= "image/jpeg":
        raise HTTPException(400, detail="Invalid file type")
    else:
        file.filename = f"{uuid.uuid4()}.jpg"
        content = await file.read()
    return {"content":content,"filename": file.filename}

