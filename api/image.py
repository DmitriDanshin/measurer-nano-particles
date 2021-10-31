from typing import List
from fastapi import APIRouter, HTTPException
from schemas.image import ImageData, ImageCreate, UnhandledImage
from fastapi import UploadFile, File, Depends
from services import image as image_service
from sqlalchemy.orm import Session
from database import get_db

router = APIRouter(
    prefix='/images'
)

descriptions = {
    "delete": "Удалить изображение из базы данных по id.",
    "get_by_id": "Получить необработанное изображение по id.",
    "get_all": "Получить все необработанные изображения",
    "handle": "Обработать изображение.",
    "handle_by_id": "Обработать изображение, которое содержится в базе данных"
}


@router.delete("/{id}", description=descriptions.get("delete"))
def delete_image(image_id: int, db: Session = Depends(get_db)):
    if not image_service.delete_image(db, image_id=image_id):
        raise HTTPException(status_code=404, detail="Image not found")
    return None


@router.get("/{id}", response_model=UnhandledImage, description=descriptions.get("get_by_id"))
def read_image(image_id: int, db: Session = Depends(get_db), image_data: bool = True):
    db_image = image_service.get_image(db, image_id=image_id, image_data=image_data)
    if db_image is None:
        raise HTTPException(status_code=404, detail="Image not found")
    return db_image


@router.post("/{id}", response_model=ImageData, description=descriptions.get("handle_by_id"))
def handle_image_database(image_id: int, data: ImageCreate = Depends(ImageCreate), db: Session = Depends(get_db)):
    db_image = image_service.handle_by_id(db=db, image_id=image_id, data=data)
    if db_image is None:
        raise HTTPException(status_code=404, detail="Image not found")
    return db_image


@router.post("/", response_model=ImageData, description=descriptions.get("handle"))
def handle_image(img: UploadFile = File(...),
                 data: ImageCreate = Depends(ImageCreate),
                 db: Session = Depends(get_db)):
    return image_service.handle_file(db=db, data=data, img=img)


@router.get("/", response_model=List[UnhandledImage], description=descriptions.get("get_all"))
def read_images(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), image_data: bool = False):
    return image_service.get_images(db, skip=skip, limit=limit, image_data=image_data)
