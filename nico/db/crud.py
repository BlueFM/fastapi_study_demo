from sqlalchemy.orm import Session

from . import models, schema


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


import hashlib
from nico.core.config import SALT


def get_password_hash(password, salt=SALT):
    hash_pwd = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 1000)
    return hash_pwd


def create_user(db: Session, user: schema.UserCreate):
    fake_hashed_password = get_password_hash(user.password)
    db_user = models.User(email=user.email, username=user.username, password_hash=str(fake_hashed_password))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_cat_infos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.StrayCatInfo).offset(skip).limit(limit).all()


def create_cat_info(db: Session, cat_info: schema.CatInfoDataInput):
    db_cat_info = models.StrayCatInfo(title=cat_info.title, description=cat_info.description,
                                      image_url=cat_info.img_url, location_lat=cat_info.location_lat,
                                      location_lng=cat_info.location_lng)
    db.add(db_cat_info)
    db.commit()
    db.refresh(db_cat_info)
    return db_cat_info
