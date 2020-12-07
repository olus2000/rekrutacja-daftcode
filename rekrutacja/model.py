from rekrutacja.db import db
from enum import Enum


class User(db.Model):
    __tablename__ = 'user'
    login = db.Column('login', db.String(64), primary_key=True)
    password = db.Column('password', db.String(94), nullable=False)


class Token(db.Model):
    __tablename__ = 'token'
    value = db.Column('value', db.String(256), primary_key=True)
    expires = db.Column('expires', db.DateTime(), nullable=False)


class Message(db.Model):
    __talbename__ = 'message'
    id = db.Column('id', db.Integer(), primary_key=True, autoincrement=True)
    content = db.Column('content', db.Unicode(160))
    edited = db.Column('edited', db.DateTime())
    views = db.Column('views', db.Integer(), default=0)
