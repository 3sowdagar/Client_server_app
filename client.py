#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
from fastapi import FastAPI, HTTPException,File,UploadFile
from fastapi.middleware.cors import CORSMiddleware
import uuid
from pathlib import Path
import shutil
import io
import cv2
import numpy as np
import uvicorn
import os
import requests
import uvicorn
import os



# In[2]:


app = FastAPI(title="Table Extractor client API")

@app.get("/")
async def read_main():
    return {"msg": "Hello Let's extract table as csv from image !!!!"}


@app.post("/post")
async def create_upload_file(file:UploadFile=File(...)):

    client_DIR="client_database"
    os.makedirs(client_DIR,exist_ok=True)
    url = "http://localhost:9001/upload-and-predict/tf/"
    file.filename=f"{uuid.uuid4()}.png"
    contents=await file.read()
    with open(os.path.join(client_DIR,str(file.filename)),"wb") as f:
        f.write(contents)
    with open(os.path.join(client_DIR,str(file.filename)),"rb") as f:
        response = requests.post(url, files={"file": f})
        #response_json,response_file=response[0],response[1]
        with open(os.path.join(client_DIR,'responce_from_server.csv'), 'wb') as f:
            f.write(response.content)
    os.remove(os.path.join(client_DIR,str(file.filename)))
    return "file_saved"



if __name__ == "__main__":
    uvicorn.run("client:app", host="0.0.0.0", port=9002, log_level="debug",
                proxy_headers=True, reload=True)




