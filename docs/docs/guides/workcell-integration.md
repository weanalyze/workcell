---
sidebar_position: 3
---

# Workcell integration

## Use workcell as a python package

Alternatively, you can import the workcell in your python project, and serve your function using an ASGI web server such as [Uvicorn](https://www.uvicorn.org/) or [FastAPI](https://fastapi.tiangolo.com/). 

Simply wrap your function with `workcell.create_app` like this:

```python
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
```

Then you can run the app using the following command:

```bash
uvicorn app:app --host 0.0.0.0 --port 7860
```
