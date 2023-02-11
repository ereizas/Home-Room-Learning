from fastapi import FastAPI, File, UploadFile
from fastapi.exceptions import HTTPException
import json, uuid

app = FastAPI()
images = []

#request for uploading the images
@app.post("/images/")
async def upload_image(file: UploadFile):
    contents = {}
    if file.content_type!= "image/jpeg":
        raise HTTPException(400, detail="Invalid file type")
    else:
        file.filename = f"{uuid.uuid4()}.jpg"
        contents = await file.read()
        images.append(contents)

    return {"filename": file.filename}

@app.get("/images/")
def read_image(file: UploadFile):
     if file.content_type!= "image/jpeg":
        raise HTTPException(400, detail="Invalid file type")

@app.post("/upload_videos")
async def upload_videos(file: UploadFile):
    if file.content_type!= "video/mp4":
        raise HTTPException(400, detail="Invalid file type")
    else:
        pass


    

if __name__ == "__main__":
    uvicorn.run(app,host="127.0.0.1",port=8000)