from sqlalchemy.orm import Session
from handler import handle_image as handle
from shutil import copyfileobj
from schemas.image import ImageCreate
from utils.to_base64 import to_base64
from models.image import Image as ImageModel


def create_image(db: Session, data: ImageCreate, img):
    with open("image.png", "wb") as buffer:
        copyfileobj(img.file, buffer)
        img_base64 = to_base64()

    if data.save:
        db_image = ImageModel(img_base64=img_base64)
        db.add(db_image)
        db.commit()
        db.refresh(db_image)

    image_data = handle(params=data)
    return image_data


def get_images(db: Session, skip: int = 0, limit: int = 100):
    return db.query(ImageModel).offset(skip).limit(limit).all()


def get_image(db: Session, image_id: int):
    return db.query(ImageModel).filter(ImageModel.id == image_id).first()


def delete_image(db: Session, image_id: int):
    image: ImageModel = db.query(ImageModel).filter(ImageModel.id == image_id).first()
    if image:
        db.delete(image)
        db.commit()
        return True
    return False
