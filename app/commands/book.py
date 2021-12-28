import click

import app.services.book as service


@click.group()
def book():
    """Commands for book"""
    pass

@book.command()
@click.option("--profile_id", required=True, type=int)
def create(profile_id):
    """Create a book"""
    created = service.create(profile_id=profile_id)
    click.echo(f"Created: {created}")

@book.command()
@click.option("-i", "--id", "identity", required=True, type=int)
@click.option("--status", required=True, type=str)
@click.option("--due_date", required=True, type=str)
@click.option("--profile_id", required=True, type=str)
@click.option("--user_id", required=True, type=int)
def update(identity, status, due_date, profile_id, user_id):
    """Update a book"""
    updated = service.update(identity=identity, status=status, due_date=due_date, profile_id=profile_id, user_id=user_id)
    click.echo(f"Updated: {updated}")

@book.command()
@click.option("-i", "--id", "identity", required=True, type=int)
def delete(identity):
    """Delete a book"""
    service.delete(identity=identity)
    click.echo(f"Deleted")

@book.command()
@click.option("-i", "--id", "identity", required=True, type=int)
def get(identity):
    """Get a book by id"""
    founded = service.get_one(identity)
    click.echo(f"Founded: {founded}")


@book.command("list")
def listAll():
    """List all books"""
    books = service.get_all()
    click.echo(f"List: {books}")
