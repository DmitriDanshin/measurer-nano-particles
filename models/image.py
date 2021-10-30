from datetime import datetime
from sqlalchemy import Column, Integer, String, Text
from database import Base


class Image(Base):
    __tablename__ = "images"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, default=f"img-{datetime.today()}")
    img_base64 = Column(Text)
