import dataclasses
import json

from flask import Blueprint, current_app, request, jsonify, make_response

from context_ import get_context
from domain.book import Book
from marshmallow import ValidationError

from views.book_shema import Book_Schema

bp = Blueprint("book", __name__)


@bp.route("/")
def get_books():
    ctx = get_context(current_app)
    books = ctx.book_service.get()
    response = make_response(Book_Schema(many=True).dump(books))
    response.headers['Content-Type'] = 'application/json'

    return response


@bp.route("/", methods=["POST"])
def add_book():
    ctx = get_context(current_app)
    try:
        book_data = Book_Schema().load(request.json)
    except ValidationError as err:
        return err.messages, 400

    book = Book(**book_data)
    try:
        book = ctx.book_service.add(book)
    except Exception as e:
        return {
            "errorrrr": repr(e),
            "data": book_data
        }

    return Book_Schema().dump(book)






    # book_data = request.get_json()
    # book = Book_Schema().load(book_data)
    # book = Book_Schema().load(**request.get_json())
    # book_id = ctx.book_service.add(book_data)
    # return #  Book_Schema().dump(book_id)


@bp.route("/<id>", methods=["DELETE"])
def delete_book(id):
    ctx = get_context(current_app)

    ctx.book_service.delete(id)

    return {}