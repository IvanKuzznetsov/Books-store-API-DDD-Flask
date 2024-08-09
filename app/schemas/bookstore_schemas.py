from marshmallow import Schema, fields


class BookHttpDto(Schema):
    class Meta:
        pages_count = fields.Int()
        fields = ["id", "title", "description", "publish_year", "pages_count"]

    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    publish_year = fields.Int()
    pages_count = fields.Int()
    created_at = fields.DateTime()
