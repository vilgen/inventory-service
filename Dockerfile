FROM python:3.12-alpine

WORKDIR /app

COPY pyproject.toml poetry.lock README.md /app/
RUN pip install poetry
RUN poetry install --no-root

COPY ./inventory_service /app/inventory_service

EXPOSE 8000

CMD ["poetry", "run", "uvicorn", "inventory_service.main:app", "--host", "0.0.0.0", "--port", "8000"]