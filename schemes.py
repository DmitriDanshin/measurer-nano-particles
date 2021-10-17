from typing import List

from pydantic import BaseModel, Field


class ImageData(BaseModel):
    image: str
    amount: int
    maxSize: int
    minSize: int
    sizes: List[int]
    mean: float
    median: int
    mode: int
