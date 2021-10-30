from typing import List
from pydantic import BaseModel
from utils.as_form import as_form


@as_form
class ImageCreate(BaseModel):
    show_size: bool = True
    show_border: bool = False
    show_contours: bool = True
    particles_size_nm: int = 200
    gaussian_accuracy: int = 11
    lower_threshold: int = 50
    upper_threshold: int = 100
    size_accuracy: int = 19
    canny: bool = False
    handle: bool = True
    save: bool = False


class ImageStatistics(BaseModel):
    sizes: List[int] = []
    amount: int = 0
    maxSize: int = 0
    minSize: int = 0
    mean: float = 0
    median: int = 0


class ImageData(ImageStatistics):
    image: str = ""


class UnhandledImage(BaseModel):
    id: int
    name: str = ""
    img_base64: str = ""

    class Config:
        orm_mode = True
