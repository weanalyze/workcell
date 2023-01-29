import pyarrow as pa
import pandas as pd
import jsonpickle


def serialize_list_with_pyarrow(names, data, types=None, legacy=False):
    """Create an arrow binary that can be loaded and manipulated from memory.

    Args:
        names (list): a list of str column names
        data (list): a list of lists containing data for each column
        types (list): an optional list of `pyarrow.type` function references.
            Types will be inferred if not provided.
        legacy (bool): if True, use legacy IPC format (pre-pyarrow 0.15). Defaults to False.

    Returns:
        bytes : a bytes object containing the arrow-serialized output.
    """
    stream = pa.BufferOutputStream()
    arrays = []

    for idx, column in enumerate(data):
        # only apply types if array is present
        kwargs = {}
        if types:
            kwargs["type"] = types[idx]
        arrays.append(pa.array(column, **kwargs))

    batch = pa.RecordBatch.from_arrays(arrays, names) # batch = pa.RecordBatch.from_pandas(dataframe)
    table = pa.Table.from_batches([batch])
    writer = pa.RecordBatchStreamWriter(
        stream, table.schema, use_legacy_format=legacy)

    writer.write_table(table)
    return stream.getvalue().to_pybytes()


def serialize_dataframe_with_pyarrow(dataframe: pd.DataFrame, types=None, legacy=False):
    """Create an arrow binary that can be loaded and manipulated from memory.

    Args:
        dataframe (pandas.DataFrame): a pandas dataframe to serialize.
        types (list): an optional list of `pyarrow.type` function references.
            Types will be inferred if not provided.
        legacy (bool): if True, use legacy IPC format (pre-pyarrow 0.15). Defaults to False.

    Returns:
        bytes : a bytes object containing the arrow-serialized output.
    """
    batch = pa.RecordBatch.from_pandas(dataframe) # batch = pa.record_batch(dataframe)
    write_options = pa.ipc.IpcWriteOptions(compression="zstd")
    sink = pa.BufferOutputStream()
    with pa.ipc.new_stream(sink, batch.schema,   options=write_options) as writer:
        writer.write_batch(batch)
    pybytes = sink.getvalue().to_pybytes()
    pybytes_str = jsonpickle.encode(pybytes, unpicklable=True, make_refs=False)
    return pybytes_str
