<!-- markdownlint-disable MD033 MD041 -->
<h1 align="center">
    Workcell
</h1>

<p align="center">
    <strong>Instantly turn your Python function into production-ready microservice.</strong>
</p>

<p align="center">
    <a href="https://pypi.org/project/workcell/" title="PyPi Version"><img src="https://img.shields.io/pypi/v/workcell?color=green&style=flat"></a>
    <a href="https://github.com/weanalyze/workcell/actions/workflows/release.yml" title="PyPi Version"><img src="https://github.com/weanalyze/workcell/actions/workflows/release.yml/badge.svg"></a> 
    <a href="https://github.com/weanalyze/workcell/actions/workflows/build-image.yml" title="PyPi Version"><img src="https://github.com/weanalyze/workcell/actions/workflows/build-image.yml/badge.svg"></a>     
    <a href="https://pypi.org/project/workcell/" title="Python Version"><img src="https://img.shields.io/badge/Python-3.8%2B-blue&style=flat"></a>
    <a href="https://github.com/weanalyze/workcell/blob/main/LICENSE" title="Project License"><img src="https://img.shields.io/badge/License-Apache2.0-blue.svg"></a>
    <a href="https://weanalyze.co">
        <img alt="website" src="https://img.shields.io/website/https/weanalyze.co?down_color=red&down_message=offline&up_message=online">
    </a>    
    <a href="https://discord.gg/jZuDU5mQZ7">
        <img alt="discord" src="https://img.shields.io/discord/1004913083812167811?label=discord">
    </a>      
</p>

<h4 align="center">
    <p>
        <b>English</b> |
        <a href="https://github.com/weanalyze/workcell/blob/main/README_zh-hans.md">简体中文</a> 
    <p>
</h4>

<p align="center">
  <a href="#getting-started">Getting Started</a> •
  <a href="#license">License</a> •
  <a href="https://github.com/weanalyze/workcell/releases">Changelog</a>
</p>

Instantly turn your Python function into delightful app and production-ready microservice, with lightweight UI to interact with. 

<img align="center" style="width: 100%" src="https://github.com/weanalyze/weanalyze-resources/blob/main/assets/workcell_intro.png?raw=true"/>

---

## Highlights

- 🔌  Instantly turn functions into microservices within seconds.
- 📈  Automatically generate user-friendly UI for interaction.
- 🤗  One-click deployment to Hugging Face Spaces.
- ☁️  Develop locally, deploy to the cloud.
- 🧩  Empower development and analysis with scalable components.
- 🦄  Get inspired by the open-source community.

## Status

| Status | Stability | Goal |
| ------ | ------ | ---- |
| ✅ | Alpha | We are testing Workcell with a closed set of customers |
| 🚧 | Public Alpha | Anyone can sign up over at weanalyze.co. But go easy on us, there are a few kinks. |
| ❌ | Public Beta | Stable enough for most non-enterprise use-cases |
| ❌ | Public | Production-ready |

We are currently in: **Alpha**. 

## Requirements

Python 3.8+

## Installation

To get started with Workcell, you can install it using `pip`:

```bash
pip install workcell
```

## Quick Start

After workcell installed, just run:

```bash
workcell hello
```

You can find an automatically generated [Swagger UI](https://github.com/swagger-api/swagger-ui) from `http://127.0.0.1:7860/docs`

And then just goto `http://127.0.0.1:7860/ui` to try your first workcell app:) 

## Guides

What happened? Workcell has created a FastAPI service and a lightweight user interface for your functions without any additional API or UI-related code. This service is ready to be deployed to the cloud as a public service, requiring minimal setup on your end. 

With Workcell, you can focus on developing your core functionality while leaving the infrastructure and deployment details to the platform.

All you need is to make sure your function is **workcell compatible**.

_💡Note: A workcell-compatible function must have an `input` parameter and return value based on [Pydantic models](https://pydantic-docs.helpmanual.io/). The input and output models are specified using [type hints](https://docs.python.org/3/library/typing.html)._

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

To start a workcell app, follow these steps:

1. Copy the above code to a file named `app.py`.

2. Create a folder, e.g. `hello_workcell`, and place the `app.py` inside.

3. Open your terminal and navigate to the folder `hello_workcell`.

4. Start the workcell app using the following command: 

```bash
workcell serve app:hello_workcell
```

Alternatively, you can import the `workcell` package and serve your function using an ASGI web server such as [Uvicorn](http://www.uvicorn.org/) or [FastAPI](https://fastapi.tiangolo.com/). Simply wrap your function with `workcell.create_app` like this:

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

Finally, run the app using the following command:

```bash
uvicorn app:app --host 0.0.0.0 --port 7860
```
_💡Note: The output will display the location where the API is being served on your local machine._

## Deployment

🤗 You can deploy your workcell to Hugging Face [Spaces](https://huggingface.co/spaces/launch) in 1-click! You'll be able to access your workcell from anywhere and share it with your team and collaborators.

### **Prepare your Hugging Face account**

First you need a Hugging Face account, and prepare your Hugging Face username and [User Access Tokens](https://huggingface.co/settings/tokens), then set environment variables like below:

```bash
export HUGGINGFACE_USERNAME={huggingface_username}
export HUGGINGFACE_TOKEN={hf_XXX}
```   

Replace `{huggingface_username}` with your actual Hugging Face username, and `{hf_XXX}` with your actual User Access Token. You can also store these environment variables in a `.env` file in your project folder for convenience.

### **Deploy Workcell**

1. Prepare you **workcell compatible** function.

2. In your project folder, package your workcell app using the following command:

```bash
workcell pack app:hello_workcell
```
_💡Note: `workcell pack {file_name}:{create_app_name}` will package your function code with a `Dockerfile` template into `.workcell` folder in your project folder._

3. Once packaged, deploy your workcell app using the following command:

```bash
workcell deploy
```

Voila! The deployment process will start, and within a few minutes, your workcell will be available on Hugging Face Spaces, accessible by a unique URL. 

## Documents

You can find more tutorials in [documents](https://weanalyze.github.io/workcell-docs/docs/quick-start).

## Examples

🎮 Get inspired and learn more about workcell by exploring our examples:

- https://github.com/weanalyze/workcell-examples

🏆 We also have a curated list for you to check out, feel free to contribute!

- https://github.com/weanalyze/best-of-workcell

## Roadmap

🗓️ Missing a feature? Have a look at our [public roadmap](https://github.com/orgs/weanalyze/projects/5/) to see what the team is working on in the short and medium term. Still missing it? Please let us know by opening an issue!

## Contacts

❓ If you have any questions about the workcell or weanalyze , feel free to email us at: support@weanalyze.co

🙋🏻 If you want to say hi, or are interested in partnering with us, feel free to reach us at: contact@weanalyze.co

😆 Feel free to share memes or any questions at Discord: https://discord.weanalyze.co

## License

Apache-2.0 License.
