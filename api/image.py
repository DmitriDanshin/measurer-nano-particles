from typing import List
from fastapi import APIRouter, HTTPException
from schemas.image import ImageData, ImageCreate, UnhandledImage
from fastapi import UploadFile, File, Depends
from services import image as image_service
from sqlalchemy.orm import Session
from database import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


router = APIRouter(
    prefix='/images'
)


@router.delete("/{id}")
def delete_image(image_id: int, db: Session = Depends(get_db)):
    if not image_service.delete_image(db, image_id=image_id):
        raise HTTPException(status_code=404, detail="Image not found")
    return None


@router.get("/{id}", response_model=UnhandledImage)
def read_image(image_id: int, db: Session = Depends(get_db)):
    db_image = image_service.get_image(db, image_id=image_id)
    if db_image is None:
        raise HTTPException(status_code=404, detail="Image not found")
    return db_image


@router.get("/", response_model=List[UnhandledImage])
def read_images(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return image_service.get_images(db, skip=skip, limit=limit)


@router.post("/", response_model=ImageData)
def handle_image(img: UploadFile = File(...),
                 data: ImageCreate = Depends(ImageCreate),
                 db: Session = Depends(get_db)):
    return image_service.create_image(db=db, data=data, img=img)
