format:
	black .
	ruff format .
	isort .

lint:
	ruff check .

test:
	pytest

validate:
	python -m validation.validate_project

build:
	python dev_tools.py

all:
	black .
	ruff format .
	isort .
	ruff check .
	pytest
	python -m validation.validate_project