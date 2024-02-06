import dataclasses
import json

from flask import Blueprint, current_app, request, jsonify

from context_ import get_context
from domain.book import Book

from views.book_shema import Book_Schema

bp = Blueprint("book", __name__)


@bp.route("/")
def get_books():
    ctx = get_context(current_app)
    book = ctx.book_service.get()
    return Book_Schema.dump(book)


@bp.route("/", methods=["POST"])
def add_book():
    ctx = get_context(current_app)

    book = Book_Schema().load(**request.json)
    book_id = ctx.book_service.add(book)
    return jsonify({"id": book_id, "book": book})


@bp.route("/<id>", methods=["DELETE"])
def delete_book(id):
    ctx = get_context(current_app)

    ctx.book_service.delete(id)

    return {}