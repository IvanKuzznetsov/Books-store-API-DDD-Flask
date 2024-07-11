import dataclasses
import json

from flask import Blueprint, current_app, request

from app.context import get_context
from app.domain.book import Book


bp = Blueprint("book", __name__)


@bp.route("/")
def get_books():
    # Используем хелпер для получения обработчика бизнес логики
    ctx = get_context(current_app)
    # Получаем через контекст по безнес логике книги и конвертируем в JSON
    return json.dumps([dataclasses.asdict(b) for b in ctx.book_service.get()])


@bp.route("/", methods=['POST'])
def add_book():
    # Получаем контекст
    ctx = get_context(current_app)
    # Декоратор dataclass генерирует дефолтный конструктор, в который
    # можно передать все поля класса (Json-словарь) и получить объект
    # но все поля обязательно должны быть заданы
    book = Book(**request.json)
    # Добавляем книгу в хранилище через контекст
    book_id = ctx.book_service.add(book)
    return {"id": book_id, "book": book}


@bp.route("/", methods=['DELETE'])
def delete_book(id):
    # Получаем контекст
    ctx = get_context(current_app)
    ctx.book_service.delete(id)
    return {}
