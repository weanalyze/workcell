import base64
from pydantic import BaseModel, Field


class SVG(BaseModel):
    data: str = Field(
        ..., title="SVG", description="A SVG plot str, will be encoded into b64 html <img> tag."
    )

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            str: lambda v: v
        }

