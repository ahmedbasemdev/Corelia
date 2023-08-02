from fastapi import APIRouter, File, UploadFile
upload_router = APIRouter()


@upload_router.get("/")
def root():
    return {"Home": "Hello"}


@upload_router.post("/uploadfile")
async def create_upload_file(file: UploadFile = File(...)):
    return {"filename": file.filename}
