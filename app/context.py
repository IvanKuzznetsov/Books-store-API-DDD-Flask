from flask import g

from infra.repository.sqlite_books_repository import SqliteBookRepository
from application.book_service import BookService


# Хелпер класс для хранения зависимостей
# В него передаем storage и book_service
class Context:
    def __init__(self):
        book_storage = SqliteBookRepository()
        self.book_service = BookService(book_storage)


def get_context(app):
    return app.config['CONTEXT']
