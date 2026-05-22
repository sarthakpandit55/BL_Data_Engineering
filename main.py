from fastapi import FastAPI
from database import engine
from models import Base
from crud import router

app = FastAPI()

Base.metadata.create_all(bind = engine)

app.include_router(router, prefix="/patients", tags=["patient router"])