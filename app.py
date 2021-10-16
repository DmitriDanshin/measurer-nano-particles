import datetime
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import shutil
import base64

import cv2

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
    # чтение изображение
    with open("image.png", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # обработка изображения
    (image, amount, max_size,
     min_size, sizes) = handle_image("image.png",
                                     gaussian_accuracy, lower_threshold, upper_threshold,
                                     size_accuracy, particles_size_nm, show_border,
                                     show_size, show_contours, canny)
    # сохранение изображение
    cv2.imwrite("image.png", image)

    # сохранение изображения в историю
    cv2.imwrite(f"images/image{amount}-{datetime.date.today()}.png", image)

    with open("image.png", "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())

    return {
        "amount": amount,
        "maxSize": max_size,
        "minSize": min_size,
        "sizes": sizes,
        "image": encoded_string
    }
