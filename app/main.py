
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app import crud, schemas
from app.dependencies import get_db
from app.routers.auth import auth_router
from app.routers.users import users_router
from app.routers.documents import doc_router


app = FastAPI(title="Real-Time Docs")
app.include_router(users_router, prefix="/users", tags=["Users"])
app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(doc_router,prefix="/doc",tags=["Docs"])

