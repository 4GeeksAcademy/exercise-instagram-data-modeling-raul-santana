import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    userId = Column(Integer, primary_key=True)
    userName = Column(String(25), unique=True)
    firstName = Column(String(30), nullable=False)
    lastName = Column(String(30), nullable=False)
    email = Column(String(40), nullable=False)
    follower = relationship("Follower", backref="follower")
    post = relationship("Post", backref="post")
    comment = relationship("Comment", backref="comment")

class Follower(Base):
    __tablename__ = 'follower'
    ID = Column(Integer, primary_key=True)
    userFromId = Column(Integer, ForeignKey('user.userId'))
    userToId = Column(Integer, ForeignKey('user.userId'))


## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
