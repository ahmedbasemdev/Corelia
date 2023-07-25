from fastapi import FastAPI,File,UploadFile
import uvicorn
from routers import upload_router,model_router
from dotenv import load_dotenv
import os

load_dotenv()


app = FastAPI()
app.include_router(upload_router)
app.include_router(model_router)



#HOST = os.environ.get("HOST")
#PORT = os.environ.get("PORT")


if __name__  == "__main__":
    uvicorn.run(app="main:app",host="0.0.0.0", port= 5000, reload=True)