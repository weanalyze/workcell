from workcell.core import Component


class Input(Component):
    message: str

class Output(Component):
    message: str


def hello_workcell(input: Input) -> Output:
    """Returns the `message` of the input data."""
    return Output(message=input.message)
