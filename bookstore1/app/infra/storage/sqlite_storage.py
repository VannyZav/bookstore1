from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from bookstore1.app.bookstore import app


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///bookstore1.db'
db.app = app
db.init_app(app)
db.create_all()


class SqliteStorage:
    def __init__(self, db_path):
        self.engine = create_engine('sqlite:///' + db_path)
        self.Session = sessionmaker(bind=self.engine)

    def get_session(self):
        return self.Session()
