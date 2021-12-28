from marshmallow import fields

from app.serializers import BaseSchema


class BookSchema(BaseSchema):
    id = fields.Int()
    due_date = fields.DateTime()
    status = fields.Str()
    profile_id = fields.Int()
    user_id = fields.Int()
