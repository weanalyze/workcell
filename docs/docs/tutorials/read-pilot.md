---
sidebar_position: 3
---

# Read pilot

Learn how to use workcell to integate with OpenAI API.

## Motivation

[OpenAI](https://openai.com/)'s GPT-3 (Generative Pre-trained Transformer 3) is a state-of-the-art language model that can generate natural language text in response to input prompts. The GPT-3 API allows developers and researchers to access this powerful language model using simple API requests, enabling them to build a wide range of applications such as chatbots, language translation systems, content generators, and more.

In this tutorial, we will built an AI-powered read pilot that generates thought-provoking discussion questions from webpage content using OpenAI GPT-3 API.

:::note
You need an [OpenAI API Key](http://beta.openai.com/) to deploy this app.
:::

## Code

The source code of this tutorial is on [Hugging Face Spaces](https://huggingface.co/spaces/jiandong/analyze_url).

The project dir as follows:

```console
➜ tree -L 2 ./              
./
├── app.py
├── requirements.txt
└── utils
    ├── extractor.py
    └── summarizer.py

2 directories, 4 files
```

## Step-by-step implementation

### Step1. Prepare an OpenAI API key

Set up an OpenAI API account and obtain an API key.

### Step2. Install dependencies

Install the openai Python library using pip.

```console
pip install openai
```

### Step3. Implement a webpage extractor

Define a function that extracts the text content from the webpage using a Python library such as [selectolax](https://github.com/rushter/selectolax).

<details>
<summary>Python file to extract webpage</summary>

```python title="{project_folder}/utils/extractor.py"
import requests
from selectolax.parser import HTMLParser
import re
from string import punctuation


def preprocess_text(text):
    text = text.lower()  # Lowercase text
    # punctuation = r'\'\":'
    text = re.sub(f"[{re.escape(punctuation)}]", "", text)  # Remove punctuation
    text = " ".join(text.split())  # Remove extra spaces, tabs, and new lines
    return text

def get_html(url):
    # request web page
    resp = requests.get(url)
    # get the response text. in this case it is HTML
    html = resp.text
    return html

def get_text(html):
    tree = HTMLParser(html)
    if tree.body is None:
        return None
    for tag in tree.css('script'):
        tag.decompose()
    for tag in tree.css('style'):
        tag.decompose()
    # get the text from the body tag
    text = tree.body.text(separator='')
    # preprocess
    text = preprocess_text(text)
    return text

def get_html_text(url):
    html = get_html(url)
    text = get_text(html)
    return text
```
</details>

### Step4. Implement a content summarizer

Define a function that uses the OpenAI client to generate discussion questions based on the extracted text. 

You may need to apply some prompt engineering techniques to ensure that the generated questions are relevant and thought-provoking.

:::tip what-is-prompt-engineering?
For example, you could use the extracted text as input to the OpenAI API and add a prefix such as "What might be some interesting discussion questions related to this passage?" or "What implications does this passage have for society?" to guide the model towards generating relevant questions. Further reading: [best-practices-for-prompt-engineering-with-openai-api](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api)
:::

<details>
<summary>Python file to summarize webpage</summary>

```python title="{project_folder}/utils/summarizer.py"
import ast
import openai
from transformers import GPT2Tokenizer

# Initialize tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

# Prompt engineering
def get_prompt(text):
    prompt_prefix = """Generate exactly 3 different and thought provoking discussion questions about given article below, and return the answers of these questions with the evidence.
    
    Desired output format: [{"Q":<question>,"A":<answer>},{"Q":<question>,"A":<answer>},{"Q":<question>,"A":<answer>}].
    """ 
    prompt_postfix ="""
    Given article content: \"""{}.\"""
    """
    prompt = prompt_prefix + prompt_postfix.format(text)
    return prompt

def limit_tokens(text, n=3000):
    # Get the first n tokens from the input text
    input_ids = tokenizer.encode(text, return_tensors="pt")
    first_n_tokens = input_ids[:, :n]
    # Convert the first n tokens back to text format
    processed_text = tokenizer.decode(first_n_tokens[0], skip_special_tokens=True)    
    return processed_text

def get_openai_completion(text):
    processed_text = limit_tokens(text)
    augmented_prompt = get_prompt(processed_text)

    try:
        result = openai.Completion.create(
            model="text-davinci-003",
            prompt=augmented_prompt,
            temperature=0.7,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            max_tokens=500,
            stream=False, 
            n=1
        )
    except:
        raise
    return result

def get_analyze(result):
    try:
        # analyze = ast.literal_eval(result["choices"][0]['text'])
        analyze = eval(result["choices"][0]['text'])
    except:
        raise    
    return analyze

def get_analyze_result(text):
    result = get_openai_completion(text)
    analyze = get_analyze(result)
    return analyze
```
</details>

### Step5. Create a workcell

Create a workcell web application that accepts a URL as input and returns a list of result generated by GPT-3.

<details>
<summary>Python file to create workcell</summary>

```python title="{project_folder}/app.py"
import os
from typing import Dict, List
from pydantic import BaseModel, Field

import openai
from utils.summarizer import get_analyze_result
from utils.extractor import get_html_text


class Input(BaseModel):
    url: str

class Output(BaseModel):
    analyze: List[Dict[str, str]] = Field(
        ..., description="A lisf of dict Q&A response, generated by OpenAI GPT3."
    )

def analyze_url(input: Input) -> Output:
    """Returns a thought provoking discussion questions from url provided, generated by OpenAI GPT3 API."""
    openai.api_key = os.getenv('SECRET_OPENAI_API_KEY')
    # return summarization
    text = get_html_text(input.url)
    analyze = get_analyze_result(text)
    output = Output(
        analyze=analyze
    )
    return output
```
</details>

### Step6. Serving or deploying

That's it! With these steps, you will have built an AI-powered read pilot that generates thought-provoking discussion questions from webpage content using OpenAI GPT-3 API.




