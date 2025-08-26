from fastapi import Depends
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.models import User,Document
from app.schemas import UserCreate,DocumentResponse,DocumentUpdate

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def create_user(db: Session, user: UserCreate):
    fake_hashed_password = get_password_hash(user.password)
    db_user = User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(User).offset(skip).limit(limit).all()

def create_doc(db: Session, user_id : int , document : Document):
    new_doc=Document(title=document.title,content=document.content,owner_id=user_id)
    db.add(new_doc)
    db.commit()
    db.refresh(new_doc)
    return new_doc

def get_doc(db: Session, doc_id: int):
    return db.query(Document).filter(Document.id==doc_id).first()

def get_docs_by_owner(db : Session , user_id : User ):
    return db.query(Document).filter(Document.owner_id == user_id).all()

def update_document(db: Session, db_doc: Document, doc_update: DocumentUpdate):
    if doc_update.title is not None:
        db_doc.title = doc_update.title
    if doc_update.content is not None:
        db_doc.content = doc_update.content
    db.add(db_doc)
    db.commit()
    db.refresh(db_doc)
    return db_doc

def delete_document(db: Session, db_doc: Document):
    db.delete(db_doc)
    db.commit()
    return
