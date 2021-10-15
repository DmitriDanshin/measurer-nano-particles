import datetime

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
        gaussian_accuracy: int = 9,
        lower_threshold: int = 50,
        upper_threshold: int = 100,
        size_accuracy: int = 19,
        canny: bool = False,
        file: UploadFile = File(...)):
    with open("image.png", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    image, amount = handle_image("image.png",
                                 gaussian_accuracy,
                                 lower_threshold,
                                 upper_threshold,
                                 size_accuracy,
                                 particles_size_nm,
                                 show_border,
                                 show_size,
                                 show_contours,
                                 canny
                                 )
    cv2.imwrite("image.png", image)
    cv2.imwrite(f"images/image{amount}-{datetime.date.today()}.png", image)
    return FileResponse("image.png", media_type="image/jpeg", filename=f"{amount}.jpg")
