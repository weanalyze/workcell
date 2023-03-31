---
sidebar_position: 2
---

# Create a workcell

## Say hello to workcell

You can start by running following command:

```bash
workcell hello
```

This command do following steps:

1. Init a `hello_workcell` workcell project in current folder.

2. Serve `hello_workcell` workcell app

Now you can visit `127.0.0.1:7860/ui` to visit a running workcell UI, or check the automatically generated Swagger UI. 

## Workcell compatible function

You have no need to implement any UI or API features yourself, if your function is **workcell compatible**, you can serve it by workcell directly.

:::tip
A workcell-compatible function must have an input parameter and return value based on [Pydantic models](https://docs.pydantic.dev/). The input and output models are specified using [type hints](https://docs.python.org/3/library/typing.html).
:::

Here is an example of a simple **workcell compatible** function:

```python
from pydantic import BaseModel

class Input(BaseModel):
    message: str

class Output(BaseModel):
    message: str

def hello_workcell(input: Input) -> Output:
    """Returns the `message` of the input data."""
    return Output(message=input.message)
```

The function `hello_workcell` can be served & deployed directly by workcell.

## Start from a template

Or if you want to explore more details, you can start from a template, use `workcell new` command as below:

```bash
workcell new {PROJECT_NAME}
```

A new folder named as `{PROJECT_NAME}` will be created into current folder. 

You can apply your change in `{PROJECT_NAME}` folder, such as modify `app.py` and rename your main function name into `FUNCTION_NAME`.

After modification, you can run workcell app by:

```bash
workcell serve {PROJECT_NAME}.app:{FUNCTION_NAME}
```

:::tip
The output will display the location where the API is being served, default running port is `7860`.
:::

