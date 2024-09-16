import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    userId = Column(Integer, primary_key=True)
    userName = Column(String(25), unique=True)
    firstName = Column(String(30),nullable=False)
    lastName = Column(String(30),nullable=False)
    email = Column(String(40), nullable=False)
    follower = relationship("Follower", backref="follower")
    post = relationship("Post", backref="post")
    comment = relationship("Comment", backref="comment")


class Follower(Base):
    __tablename__ = 'follower'
    ID = Column(Integer, primary_key=True)
    userFromId = Column(Integer, ForeignKey('user.userId'))
    userToId = Column(Integer, ForeignKey('user.userId'))
     

class Post(Base):
    __tablename__ = 'post'
    ID = Column(Integer, primary_key=True)
    userId = Column(Integer, ForeignKey('user.userId'))
    media = relationship("Media", backref="media")
    comment = relationship("Comment", backref="comment")
    

class Media(Base):
    __tablename__ = 'media'
    ID = Column(Integer, primary_key=True)
    type = Column(String)
    url = Column(String(50))
    postId = Column(Integer, ForeignKey('post.ID'))


class Comment(Base):
    __tablename__ = 'comment'
    ID = Column(Integer, primary_key=True)
    commentText = Column(String(120))
    authorId = Column(Integer, ForeignKey('user.userId'))
    postId = Column(Integer, ForeignKey('post.ID'))


    def to_dict(self):
        return {}


## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
