from marshmallow import fields

from app.serializers import BaseSchema


class BookProfileSchema(BaseSchema):
    id = fields.Int()
    title = fields.Str()
    author = fields.Str()
