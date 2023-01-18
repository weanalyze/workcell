import pyarrow as pa
import pandas as pd
import jsonpickle
from pydantic import BaseModel, Field

from typing import TypeVar
PandasDataFrameType = TypeVar('pandas.core.frame.DataFrame')


def serialize_with_pyarrow(dataframe: pd.DataFrame):
    batch = pa.record_batch(dataframe)
    write_options = pa.ipc.IpcWriteOptions(compression="zstd")
    sink = pa.BufferOutputStream()
    with pa.ipc.new_stream(sink, batch.schema,   options=write_options) as writer:
        writer.write_batch(batch)
    pybytes = sink.getvalue().to_pybytes()
    pybytes_str = jsonpickle.encode(pybytes, unpicklable=True, make_refs=False)
    return pybytes_str


class PandasDataFrame(BaseModel):
    data: PandasDataFrameType = Field(
        ..., title="Pandas dataframe", description="A pandas dataframe encode in Arrow format."
    )

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            pd.DataFrame: lambda v: serialize_with_pyarrow(v)
        } 