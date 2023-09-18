from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from ..core.config import db_config
from . import crud, models, schema
from .database import DBClient

db = DBClient(db_config=db_config)

models.Base.metadata.create_all(bind=engine)

app = FastAPI()