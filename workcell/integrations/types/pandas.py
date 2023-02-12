import pandas as pd
from pydantic import Field
from workcell.core.components import Component
from workcell.core.serialization import serialize_dataframe_with_pyarrow

from typing import TypeVar
PandasDataFrameType = TypeVar('pandas.core.frame.DataFrame')


class PandasDataFrame(Component):
    data: PandasDataFrameType = Field(
        ..., title="Pandas dataframe", description="A pandas dataframe, will be encoded in Arrow format."
    )

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            pd.DataFrame: lambda v: serialize_dataframe_with_pyarrow(v)
        } 