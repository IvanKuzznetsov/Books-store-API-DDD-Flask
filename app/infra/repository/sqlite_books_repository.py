from dataclasses import dataclass
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

from infra.repository.books_repository import BookRepository

from domain.book import Book
from sqlalchemy import func

db = SQLAlchemy()


class Books(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String(255))
    publish_year = db.Column(db.Integer)
    pages_count = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=func.now())


class SqliteBookRepository(BookRepository):
    def __init__(self):
        pass

    def add(self, book: Books):
        db.session.add(book)
        db.session.commit()
        return book.id

    def get_all(self):
        return Books.query.all()

    def get(self, id: int):
        return Books.query.get(id)

    def update(self, book: Books):
        db.session.merge(book)
        db.session.commit()

    def delete(self, id: int):
        book = Books.query.get(id)
        db.session.delete(book)
        db.session.commit()
