from flask import g

from app.application.book_service import BookService
from app.infra.storage.mem_storage import MemoryStorage


# Хелпер класс для хранения зависимостей
# В него передаем storage и book_service
class Context:
    def __init__(self):
        book_storage = MemoryStorage()
        self.book_service = BookService(book_storage)


def get_context(app):
    return app.config['CONTEXT']
