from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    documents = relationship("Document", back_populates="owner")
    collaborations = relationship(
        "Document", secondary="document_collaborators", back_populates="collaborators"
    )

class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String, default="")
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="documents")
    collaborators = relationship(
        "User", secondary="document_collaborators", back_populates="collaborations"
    )

class DocumentCollaborator(Base):
    __tablename__ = "document_collaborators"
    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    document_id = Column(Integer, ForeignKey("documents.id"), primary_key=True)