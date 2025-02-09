# ninja-api-bookstore

Project using Django-Ninja to create a simple API for a bookstore.

## Installation

```bash
poetry install
```

## Migrations
Run the following command to create the database and tables:
```bash
poetry run python manage.py migrate
```

## Running
To run the API on an ASGI server, use the following command:
```bash
poetry run uvicorn bookstore.asgi:application --reload
# or, if the venv is activated
uvicorn bookstore.asgi:application --reload
```
The following routes are available:
- `/api/hello` - Say hello.
- `/api/say-after` - Say a message after a delay (params: `delay`, `msg`).
    - `/api/say-sync` - Say a message after a delay, synchronously.
- `/api/books/` - List all books
- `/api/books/{id}` - Retrieve a book by id

## Testing

```bash
poetry run pytest
```

Test concurrent model using [ab](https://httpd.apache.org/docs/2.4/programs/ab.html):

```bash
 ab -c 100 -n 1000 "http://localhost:8000/api/say-after?delay=3&msg=hello"
```