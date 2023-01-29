import jsonpickle
import perspective
import pandas as pd
from pydantic import BaseModel, Field

from typing import TypeVar
PandasDataFrameType = TypeVar('pandas.core.frame.DataFrame')


def serialize_dataframe_with_persepective(dataframe: pd.DataFrame):
    """Create a perspective table that can be loaded and manipulated from memory.

    Args:
        dataframe (pandas.DataFrame): a pandas dataframe to serialize.

    Returns:
        pybytes_str : a string object containing the perspective-serialized output.
    """
    table = perspective.Table(dataframe)
    pybytes = table.view().to_arrow()
    pybytes_str = jsonpickle.encode(pybytes, unpicklable=True, make_refs=False)
    return pybytes_str


class PerspectiveTable(BaseModel):
    data: PandasDataFrameType = Field(
        ..., title="Pandas dataframe", description="A pandas dataframe, will be converted into perspective table, encoded in Arrow format."
    )

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            pd.DataFrame: lambda v: serialize_dataframe_with_persepective(v)
        } 