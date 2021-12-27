import click

import app.services.user as service


@click.group()
def user():
    """Commands for user"""
    pass


@user.command()
@click.option("--firstname", required=True, type=str)
@click.option("--lastname", required=True, type=str)
def create(firstname, lastname):
    """Create a user"""
    created = service.create(firstname=firstname, lastname=lastname)
    click.echo(f"Created: {created}")


@user.command()
@click.option("-i", "--id", "identity", required=True, type=int)
def get(identity):
    """Get a user by id"""
    founded = service.get(identity)
    click.echo(f"Founded: {founded}")


@user.command("list")
def listAll():
    """List all users"""
    users = service.getAll()
    click.echo(f"List: {users}")


@user.command()
@click.option("-i", "--id", "identity", required=True, type=int)
@click.option("--firstname", required=True, type=str)
@click.option("--lastname", required=True, type=str)
def update(identity, firstname, lastname):
    """Update a user by id"""
    updated = service.update(identity=identity, firstname=firstname, lastname=lastname)
    click.echo(f"Updated: {updated}")


@user.command()
@click.option("-i", "--id", "identity", required=True, type=int)
def delete(identity):
    """Delete a user by id"""
    service.delete(identity)
    click.echo("Deleted")


@user.command()
@click.option("-u", "--user-id", required=True, type=int)
@click.option("-b", "--book-id", required=True, type=int)
def borrow(user_id, book_id):
    """User borrow a book from the library"""
    service.borrow_book(user_id=user_id, book_id=book_id)
    click.echo("Success")


@user.command("return")
@click.option("-u", "--user-id", required=True, type=int)
@click.option("-b", "--book-id", required=True, type=int)
def return_book(user_id, book_id):
    """User return a book to the library"""
    service.return_book(user_id=user_id, book_id=book_id)
    click.echo("Success")


@user.command()
@click.option("-u", "--user-id", required=True, type=int)
def borrowing_list(user_id):
    """List the borrowing list of a user by user id"""
    borrowing = service.borrowing_list(user_id=user_id)
    click.echo(f"Borrowing list: {borrowing}")
