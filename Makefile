.PHONY: install run shell

install:
	poetry install

run:
	poetry run uvicorn inventory_service.main:app --reload

shell:
	poetry shell

ruff:
	poetry run ruff check .

ruff-fix:
	poetry run ruff check --fix .

rm-poetry-lock:
	rm poetry.lock
	poetry lock