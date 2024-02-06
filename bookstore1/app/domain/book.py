
from sqlalchemy.orm import Mapped, mapped_column

from infra.storage.sqlite_storage import db


class Book(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(unique=True)
    author: Mapped[str]
    publish_year: Mapped[int]
    pages_count: Mapped[int]