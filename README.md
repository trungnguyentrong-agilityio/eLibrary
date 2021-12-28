# eLibrary

## Target:
- Understanding the syntax and work flow of Python
- Understanding how to work with Postgres and SQLAlchemy

## Feature:
- Create a command line for book management
    - Create/Read/Update/Delete books
    - Create/Read/Update/Delete users
    - A user can borrow and return books
    - List all users who are borrowing books
    - List all books that are borrowing by a user

## Database design:
- [Diagram](https://dbdiagram.io/d/61c44f8c3205b45b73ca3fa1)

## How to start:
1. Run `cp env_sample .env`
2. Run `make setup-cli`

## Database Migrations

This service is using [Alembic](https://alembic.sqlalchemy.org/en/latest/index.html) for database migrations.

Check the following for common use cases:
```bash
make db-gen-migration NAME="message" # generate migration
make db-upgrade # upgrade to later version of migrations
```
## How to use the command line

Using `elib <command name> --help` to know how to run commands

List of commands:
- book
    - create (Create a book)
    - delete (Delete a book)
    - get (Get a book by id)
    - list (List all books)
    - update (Update a book)
- profile
    - create (Create a book profile)
    - delete (Delete a book profile)
    - get (Get a book profile by id)
    - list (List all book profile)
    - update (Update a book profile)
- user
    - create (Create a user)
    - delete (Delete a user by id)
    - get (Get a user by id)
    - list (List all users)
    - update (Update a user by id)
    - borrow (User borrow a book from the library)
    - borrowing_list (List the borrowing list of a user by user id)
    - return (User return a book to the library)
