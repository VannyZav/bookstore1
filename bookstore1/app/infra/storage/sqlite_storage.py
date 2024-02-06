from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# from domain.book import Book


# from bookstore1.app.bookstore import app


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)

# app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///bookstore1.db'
# db.app = app

# db.init_app(app)



class SqliteStorage:
    def __init__(self, db_path):
        self.engine = create_engine('sqlite:///' + db_path)
        self.Session = sessionmaker(bind=self.engine)

    def get_session(self):
        return self.Session()

    def get(self):
        try:
            query = db.session.query().all()
            return query
        except NoResultFound as NoRes:
            sub_report_id = []
            return sub_report_id

    def add(book):
        db.session.add(book)
        db.session.commit()
