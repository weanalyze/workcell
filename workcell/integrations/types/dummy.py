from pydantic import BaseModel


class DummyInput(BaseModel):
    """
    A dummy class for empty intput.
    """
    pass

class DummyOutput(BaseModel):
    """
    A dummy class for empty output.
    """
    pass
