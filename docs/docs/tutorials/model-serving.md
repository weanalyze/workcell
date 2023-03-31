---
sidebar_position: 2
---

# Model serving

A simple t5 model serving app by huggingface

```python
from pydantic import BaseModel
from transformers import pipeline


class Input(BaseModel):
    text: str

class Output(BaseModel):
    text: str

pipe_flan = pipeline("text2text-generation", model="google/flan-t5-small")

def model_serving_t5(input: Input) -> Output:
    """Returns the output of the `google/flan-t5-small` model."""
    model_output = pipe_flan(input.text)
    output = Output(text=model_output[0]["generated_text"])
    return output

```