from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from nico.core.config import DB_CONFIG
from . import crud, models, schema
from .database import DBClient

db = DBClient(db_config=DB_CONFIG)



router = APIRouter()


def get_db():
    try:
        dbsession = db.SessionLocal
        yield dbsession
    finally:
        dbsession.close()


@router.post("/user/", response_model=schema.User)
async def create_user(user: schema.UserCreate, dbsession: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(dbsession, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=dbsession, user=user)


@router.get("/user/{user_id}", response_model=schema.User)
async def read_user(user_id: int, dbsession: Session = Depends(get_db)):
    db_user = crud.get_user(dbsession, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.get("/cats/", response_model=schema.CatInfoResponse)
async def read_cats(skip: int = 0, limit: int = 100, dbsession: Session = Depends(get_db)):
    cats = crud.get_cat_infos(dbsession, skip=skip, limit=limit)
    return {"cats": cats}




