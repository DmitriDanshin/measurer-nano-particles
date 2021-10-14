from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import shutil

import cv2

from starlette.responses import FileResponse

from handler import handle_image

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/")
def read_image(
        show_size: bool = True,
        show_border: bool = False,
        show_contours: bool = True,
        particles_size_nm: int = 200,
        gaussian_accuracy: int = 25,
        blur_accuracy: int = 60,
        size_accuracy: int = 19,
        file: UploadFile = File(...)):
    with open("image.png", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    image, amount = handle_image("image.png",
                                 gaussian_accuracy,
                                 blur_accuracy,
                                 size_accuracy,
                                 particles_size_nm,
                                 show_border,
                                 show_size,
                                 show_contours
                                 )
    cv2.imwrite("image.png", image)
    return FileResponse("image.png", media_type="image/jpeg", filename=f"{amount}.jpg")
