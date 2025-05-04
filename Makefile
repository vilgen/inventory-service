.PHONY: install run shell

install:
	poetry install

run:
	poetry run uvicorn inventory_service.main:app --reload

shell:
	poetry shell