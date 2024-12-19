install:
	poetry install --no-root

run:
	poetry run python src/__main__.py

test:
	poetry run pytest

lint:
	poetry run flake8 .