# API Сервис "Магазин книг" на Flask (homework)
Сервис позволяет добавлять книги в хранилище, получать книгу по id, получать список всех книг, 
а также изменять информацию о книге и удалять книгу по id. Книга содержит id, название, описание, год издания
и количество страниц. Хранение осуществляется в базе данных  SQLite с помощью SQLAlchemy. Паттерн проектирования
Domain-Driven Design (DDD).

Запуск приложения
-
- Склонируйте репозиторий себе на ПК
- Откройте проект, создайте и активируйте виртуальное окружение
- Установите зависимости из файла requirements.txt
- Для запуска приложения запустите файл bookstore.py

Добавление книги
-
- Откройте Postman
- Нажмите "Создать новый запрос", выберите "http-запрос"
- Выберите метод POST
- Введите URL: http://localhost:5000/books
- Перейдите во вкладку "Body", выберите raw и справа из выпадающего списка "JSON"
- Введите информацию о книге в формате {"title":"thebook", "description": "a book", "publish_year":2020, "pages_count": 100}
- Нажмите Send (Отправить)
- Вернется JSON c информацией о книге


Получение списка книг
-
- Выберите метод GET
- Введите URL: http://localhost:5000/books
- Нажмите Send
- Вернется список книг

Получение одной книги по id
- 
- Выберите метод GET
- Введите URL: http://localhost:5000/books/<id_книги>
- Нажмите Send
- Вернется указанная книга

Изменение книги
-
- Выберите метод PUT
- Введите URL: http://localhost:5000/books/<id_книги>
- Перейдите во вкладку "Body", выберите raw и справа из выпадающего списка "JSON"
- Введите новые данные в формате {"title":"thebook2", "description": "a book", "publish_year":2024, "pages_count": 200}
- Нажмите Send
- Вернется изменённая книга

Удаление книги 
-
- Выберите метод DELETE
- Введите URL: http://localhost:5000/books/<id_книги>
- Нажмите Send
