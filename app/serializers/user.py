from marshmallow import fields

from app.serializers import BaseSchema


class UserSchema(BaseSchema):
    id = fields.Int()
    firstname = fields.Str()
    lastname = fields.Str()


class BookSchema(BaseSchema):
    id = fields.Int()
    status = fields.Str()
    due_date = fields.DateTime()


class UserBorrowingSchema(BaseSchema):
    id = fields.Int()
    firstname = fields.Str()
    lastname = fields.Str()
    book = fields.Nested(BookSchema, many=True)
