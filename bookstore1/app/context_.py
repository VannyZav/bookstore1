from flask import g

from bookstore1.app.application.book_service import BookService
from infra.storage.mem_storage import MemoryStorage
# from infra.storage.sqlite_storage import SQLiteStorage


class Context_:
    def __init__(self):
        book_storage = MemoryStorage()
        self.book_service = BookService(book_storage)


def get_context(app):
    return app.config["CONTEXT"]