from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.schemas import DocumentResponse, DocumentCreate, DocumentUpdate
from app.crud import create_doc,get_docs_by_owner,get_doc,update_document,delete_document
from app.routers.auth import get_current_user
from app.models import Document,User

doc_router = APIRouter()

@doc_router.post("/",response_model=DocumentResponse,status_code=status.HTTP_201_CREATED)
def create_doc(document : DocumentCreate, db : Session = Depends(get_db()), user : User = Depends(get_current_user())):
    return create_doc(db, user.id , document)

@doc_router.get("/", response_model=List[DocumentResponse])
def read_documents(db: Session = Depends(get_db),
                   current_user: User = Depends(get_current_user)):
    return get_docs_by_owner(db, current_user.id)

@doc_router.get("/{doc_id}", response_model=DocumentResponse)
def read_document(doc_id: int,
                  db: Session = Depends(get_db),
                  current_user: User = Depends(get_current_user)):
    db_doc = get_doc(db, doc_id)
    if not db_doc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Document not found")
    if db_doc.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to view this document")
    return db_doc


@doc_router.put("/{doc_id}", response_model=DocumentResponse)
def update_document(doc_id: int, doc_update: DocumentUpdate,
                    db: Session = Depends(get_db),
                    current_user: User = Depends(get_current_user)):
    db_doc = get_doc(db, doc_id)
    if not db_doc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Document not found")
    if db_doc.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Only owner can edit the document")
    return update_document(db, db_doc, doc_update)

@doc_router.delete("/{doc_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_document(doc_id: int,
                    db: Session = Depends(get_db),
                    current_user: User = Depends(get_current_user)):
    db_doc = get_doc(db, doc_id)
    if not db_doc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Document not found")
    if db_doc.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Only owner can delete the document")
    delete_document(db, db_doc)
    return