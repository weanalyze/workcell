from pydantic import BaseModel, Field
from workcell.integrations.types import FileContent


class ImageInput(BaseModel):
    image_file: FileContent = Field(..., mime_type="image/png")


class ImageOutput(BaseModel):
    image_file: FileContent = Field(..., mime_type="image/png")
