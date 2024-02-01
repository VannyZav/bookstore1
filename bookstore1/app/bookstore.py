from flask import Flask

from views.book import bp as book_bp
from context_ import Context_


def create_app():
    app = Flask(__name__)
    app.register_blueprint(book_bp, url_prefix="/books")
    app.config["CONTEXT"] = Context_()

    return app


app = create_app()

if __name__ == "__main__":
    app.run()