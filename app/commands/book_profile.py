import click

import app.services.book_profile as service


@click.group()
def profile():
    """Commands for book profile"""
    pass

@profile.command()
@click.option("--author", required=True, type=str)
@click.option("--title", required=True, type=str)
def create(author, title):
    """Create a book profile"""
    created = service.create(author=author, title=title)
    click.echo(f"Created: {created}")

@profile.command()
@click.option("-i", "--id", "identity", required=True, type=int)
@click.option("--author", required=True, type=str)
@click.option("--title", required=True, type=str)
def update(identity, author, title):
    """Update a book profile"""
    updated = service.update(identity=identity, author=author, title=title)
    click.echo(f"Updated: {updated}")

@profile.command()
@click.option("-i", "--id", "identity", required=True, type=int)
def delete(identity):
    """Update a book profile"""
    service.delete(identity=identity)
    click.echo(f"Deleted")

@profile.command()
@click.option("-i", "--id", "identity", required=True, type=int)
def get(identity):
    """Get a book profile by id"""
    founded = service.get_one(identity)
    click.echo(f"Founded: {founded}")


@profile.command("list")
def listAll():
    """List all book profile"""
    users = service.get_all()
    click.echo(f"List: {users}")
