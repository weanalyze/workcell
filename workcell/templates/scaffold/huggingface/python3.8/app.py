from pydantic import BaseModel
import workcell

class Input(BaseModel):
    message: str

class Output(BaseModel):
    message: str

def hello_workcell(input: Input) -> Output:
    """Returns the `message` of the input data."""
    return Output(message=input.message)

app = workcell.create_app(hello_workcell)