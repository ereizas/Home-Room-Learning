from fastapi import FastAPI, File, UploadFile
from fastapi.responses import Response
from fastapi.exceptions import HTTPException
import uuid, os, uvicorn, io, PIL

app = FastAPI()
current_image = 0


#request for uploading the images
@app.post("/images/")
def upload_image(file: UploadFile=File()):
    if file.content_type!= "image/jpeg":
        raise HTTPException(400, detail="Invalid file type")
    #file.filename = f"{uuid.uuid4()}.jpg"
    print(file.file.read())
    current_image = PIL.Picture.frombytes(io.BinaryIO(file.file.read()))
    print(current_image)
    
    #decode for JSON compatibality
    return {"data":current_image,"filename": file.filename}


    

if __name__ == "__main__":
    uvicorn.run(app,host="127.0.0.1",port=8000)