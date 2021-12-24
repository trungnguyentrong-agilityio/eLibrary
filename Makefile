#!make
include .env

## Variables ##
app_name := e-library
postgres_image := postgres
venv := .venv

## Install ##
install: venv
	pipenv --version &> /dev/null || pip install pipenv
	pipenv run pip install --upgrade pip
	pipenv install --dev

venv:
	mkdir .venv

## Setup & Run ##
run-db:
	docker run --name $(app_name)-db \
		-e POSTGRES_USER=${POSTGRES_USER} \
		-e POSTGRES_PASSWORD=${POSTGRES_PASSWORD} \
		-e POSTGRES_DB=${POSTGRES_DB} \
		-p 5432:5432 -d $(postgres_image) \
		|| docker start $(app_name)-db

setup-cli: install run-db
	pipenv install --editable .
	pipenv shell

## Migration ##
db-gen-migration:
	pipenv run alembic revision --autogenerate -m $(NAME)

db-upgrade:
	pipenv run alembic upgrade head
