from flask import Flask

from infra.repository.sqlite_books_repository import db
from context import Context
from views.book import bp as book_bp


# Хелпер для создания приложения Flask
def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(book_bp, url_prefix="/books")
    app.config["CONTEXT"] = Context()
    return app


app = create_app()


if __name__ == "__main__":
    app.run()

# Хелпер для запуска flask сервисов
# flask --app bookstore --debug run
# Debug перезапускает сервис при изменении кода
