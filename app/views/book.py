import dataclasses
import json

from flask import Blueprint, current_app, request

from context import get_context
from infra.repository.sqlite_books_repository import Books
from schemas.bookstore_schemas import BookHttpDto

bp = Blueprint("book", __name__)


@bp.route("/")
def get_books():
    # Используем хелпер для получения обработчика бизнес логики
    ctx = get_context(current_app)
    # Получаем через контекст по бизнес логике книги и конвертируем в JSON
    return [BookHttpDto().dump(book) for book in ctx.book_service.get_all()]


@bp.route("/<id>")
def get_book_by_id(id):
    # Используем хелпер для получения обработчика бизнес логики
    ctx = get_context(current_app)
    # Получаем через контекст по бизнес логике книгу и конвертируем в JSON
    book = ctx.book_service.get(id)
    return {"book": BookHttpDto().dump(book)}


@bp.route("/", methods=['POST'])
def add_book():
    # Получаем контекст
    ctx = get_context(current_app)
    # Mожно передать все поля класса (Json-словарь) и получить объект
    # но все поля обязательно должны быть заданы
    book = Books(**request.json)
    # Добавляем книгу в хранилище через контекст
    book_id = ctx.book_service.add(book)
    return {"book": BookHttpDto().dump(book)}


@bp.route("/<id>", methods=['PUT'])
def update_book(id):
    # Получаем контекст
    ctx = get_context(current_app)
    # Можно передать все поля класса (Json-словарь) и получить объект
    # но все поля обязательно должны быть заданы
    book = Books(id=id, **request.json)
    # Обновляем книгу в хранилище через контекст
    book_id = ctx.book_service.update(book)
    return {"book": BookHttpDto().dump(book)}


@bp.route("/<id>", methods=['DELETE'])
def delete_book(id):
    # Получаем контекст
    ctx = get_context(current_app)
    ctx.book_service.delete(id)
    return {"response": "deleted"}
