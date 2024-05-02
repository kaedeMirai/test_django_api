POETRY = ./.venv/bin/poetry
PYTHON = ./.venv/bin/python

venv:
	@rm -rf .venv || true && \
	python3.11 -m venv .venv && \
	.venv/bin/pip install poetry

#Создание виртуального окружения и установка всех зависимостей
build_dev:
	${POETRY} install --no-root

#Запуск БД postgresql в докере.
run_db:
	docker-compose up -d

#запуск приложения django
run_dev:
	${PYTHON} bookstore/manage.py runserver

run_dev_websocket:
	cd bookstore/ && \
	daphne bookstore.asgi:application

#Выполнение миграций
migrate:
	${PYTHON} bookstore/manage.py migrate

#создание суперпользователя
createsuperuser:
	${PYTHON} bookstore/manage.py createsuperuser

#запуск тестов
run_test:
	${PYTHON} bookstore/manage.py test books

create_test_data:
	docker cp ./testdata.sql postgres:/testdata.sql && \
    docker-compose exec postgres psql -U admin -d books -f ./testdata.sql && \
    docker exec -it postgres rm /testdata.sql
