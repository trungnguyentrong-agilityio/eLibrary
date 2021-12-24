# eLibrary

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
