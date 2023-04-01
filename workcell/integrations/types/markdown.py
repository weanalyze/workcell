import json
from pydantic import BaseModel, Field


class MarkdownMixin(BaseModel):
    data: str = Field(
        ...,
        title="Markdown Mixin",
        description="A markdown which data is encoded in json format.",
    )

    class Config:
        arbitrary_types_allowed = True
