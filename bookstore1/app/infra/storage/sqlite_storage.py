from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def setup_db(app, database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


class SQLite_storage:

    def get(self):
        pass

    def add(self):
        pass

    def delete(self, id):
        pass
