import pyarrow as pa
import pandas as pd
import perspective
from pydantic import BaseModel, Field

from typing import TypeVar
PerspectiveTableType = TypeVar('pandas.core.frame.DataFrame')


class PerspectiveTable(BaseModel):
    data: PerspectiveTableType = Field(
        ..., title="Perspective dataframe", description="A perspective table, will be encoded in Arrow format."
    )

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            perspective.Table: lambda v: pa.Table.from_pandas(v)
        } 