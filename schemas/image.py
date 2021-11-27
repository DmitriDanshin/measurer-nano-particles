from typing import List
from pydantic import BaseModel
from utils.as_form import as_form


@as_form
class ImageCreate(BaseModel):
    show_size: bool = True
    show_border: bool = False
    show_contours: bool = True
    particles_size_nm: int = 200
    gaussian_accuracy_width: int = 7
    gaussian_accuracy_height: int = 7
    lower_threshold: int = 50
    upper_threshold: int = 100
    size_accuracy: int = 10
    show_midpoints: bool = True
    user_contours: str = "[[[123, 10], [11, 54], [257, 1534], [125, 1535]]," \
                         " [[123, 43], [11, 43], [257, 43], [125, 1535]]]"
    excluded_contours: str = "[[[125, 10], [11, 54], [257, 1534], [125, 1535]]," \
                             "[[123, 43], [11, 43], [257, 43], [125, 1535]]]"
    canny: bool = False
    handle: bool = True
    save: bool = False


class ImageStatistics(BaseModel):
    sizes: List = []
    amount: int = 0
    maxSize: int = 0
    minSize: int = 0
    mean: float = 0
    median: int = 0
    contours: list = []


class ImageData(ImageStatistics):
    image: str = ""


class UnhandledImage(BaseModel):
    id: int
    name: str = ""
    img_base64: str = ""

    class Config:
        orm_mode = True
