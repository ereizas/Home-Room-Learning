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

@app.post("/download_images")
def upload_download_image(file: UploadFile):
     if file.content_type!= "image/jpeg":
        raise HTTPException(400, detail="Invalid file type")





    

if __name__ == "__main__":
    uvicorn.run(app,host="127.0.0.1",port=8000)