from flask import Flask
from context import Context
from views.book import bp as book_bp


# Хелпер для создания приложения Flask
def create_app():
    app = Flask(__name__)
    app.register_blueprint(book_bp, url_prefix="/books")
    app.config["CONTEXT"] = Context()
    return app


app = create_app()


# Хелпер для запуска flask сервисов
# flask --app bookstore --debug run
# Debug перезапускает сервис при изменении кода
