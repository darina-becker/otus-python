"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""

from ast import Str
from cgitb import text
from enum import unique
import os
from turtle import back, title
from requests import session

from sqlalchemy import ForeignKey, PrimaryKeyConstraint, Column, String, Integer, Text
from sqlalchemy.orm import declarative_base, sessionmaker, scoped_session, relationship
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine


PG_CONN_URI = a = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://postgres:password@localhost/postgres"

engine = create_async_engine(PG_CONN_URI, echo=True)

Base = declarative_base(bind=engine)

Session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

class User(Base):
    __tablename__ = 'User'

    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False)
    username = Column(String(32), unique=True, nullable=False)
    email = Column(String(32), unique=True, nullable=False)

    posts = relationship("Post", back_populates="user")

class Post(Base):
    __tablename__ = 'Post'

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    body = Column(Text, nullable=False)

    user_id = Column(Integer, ForeignKey("User.id"), nullable=False, unique=False, index=True)

    user = relationship("User", back_populates="posts")
