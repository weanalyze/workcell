import pandas as pd
from pydantic import BaseModel, Field
from workcell.core.serialization import serialize_dataframe_with_persepective

from typing import TypeVar
PandasDataFrameType = TypeVar('pandas.core.frame.DataFrame')


class PerspectiveTable(BaseModel):
    data: PandasDataFrameType = Field(
        ..., title="Pandas dataframe", description="A pandas dataframe, will be converted into perspective table, encoded in Arrow format."
    )

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            pd.DataFrame: lambda v: serialize_dataframe_with_persepective(v)
        } 