from marshmallow import Schema, fields


class Book_Schema(Schema):
    id = fields.Int()
    title = fields.Str()
    author = fields.Str()
    publish_year = fields.Int(required=False)
    pages_count = fields.Int(required=False)
