# Тестовое задание.

Выполненные задачи:

1. Создано 4 модели: Book, Author, Genre, Publisher.
2. Добавлены миграции.
3. Реализован сервис REST API с методами POST, PUT, DELETE, GET для созданных моделей.
4. Документация оформлена OpenAPI (swagger).
5. Реализована админка для моделей.
6. Реализована страница с навигацией по приложению.
7. Реализован пример вызова endpoint для создания и просмотра данных из таблицы Book с использованием WebSocket


# Инструкция по запуску проекта (*linux)
1. Склонировать репозиторий:
2. Создать файл .env. Скопировать .env.example в .env (либо переименовать .env.example).
3. В командной строке запустить проект:

    ```
    make venv - для создания виртуального окружения и установки всех зависимостей с помощью poetry.
    make run_db - для поднятия базы данных в docker.
    make run_dev - для запуска приложения локально.
    make migrate - для выполнения миграций.
    make createsuperuser - для создания супер пользователя.


    make run_dev_websocket - для запуска приложения с помощью daphne для тестирования работы API с помощью вебсокета.


    make run_test - для запуска тестов.
    make create_test_data - для заполнения БД тестовыми данными.
    ```

4. Ссылка на начальную страницу с навигацией по приложению:

http://127.0.0.1:8000/


p.s. При запуске приложения через daphne статика не подтягивается. Nginx не стал добавлять. Для сохранения статики удобно запустить сначала через run_dev, а уже после run_dev_websocket.
