from fastapi import FastAPI,File,UploadFile
import uvicorn
from routers import upload_router,model_router
from config import settings
import os




app = FastAPI()
app.include_router(upload_router)
app.include_router(model_router)





if __name__  == "__main__":

    uvicorn.run(app="main:app",host=settings.HOST, port= settings.PORT, reload=settings.RELOAD)