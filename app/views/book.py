import dataclasses
import json

from flask import Blueprint, current_app, request

from app.domain.book import Book


bp = Blueprint("book", __name__)


@bp.route("/")
def get_books():
    pass


@bp.route("/", methods=['POST'])
def add_book():
    pass


@bp.route("/", methods=['DELETE'])
def delete_book(id):
    pass
