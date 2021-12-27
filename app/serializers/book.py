from marshmallow import fields

from app.serializers import BaseSchema


class BookSchema(BaseSchema):
    id = fields.Int()
    due_date = fields.DateTime()
    profile_id = fields.Int()
    user_id = fields.Int()
