from datetime import datetime
from ninja import Schema

class HelloResponse(Schema):
    msg: str


class BaseSchema(Schema):
    id: int
    created_at: datetime
    updated_at: datetime | None
    is_deleted: bool
