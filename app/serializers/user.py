from marshmallow import fields

from app.serializers import BaseSchema


class UserSchema(BaseSchema):
    id = fields.Int()
    firstname = fields.Str()
    lastname = fields.Str()
