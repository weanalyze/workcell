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

## ⚡ Highlights

- 🔌  Instantly turn functions into microservices within seconds.
- 📈  Automatically generate user-friendly UI for interaction.
- 🤗  One-click deployment to Hugging Face Spaces.
- ☁️  Develop locally, deploy to the cloud.
- 🧩  Empower development and analysis with scalable components.
- 🦄  Get inspired by the open-source community.

## ⏰ Status

| Status | Stability | Goal |
| ------ | ------ | ---- |
| ✅ | Alpha | We are testing Workcell with a closed set of customers |
| ✅ | Public Alpha | Anyone can sign up over at weanalyze.co. But go easy on us, there are a few kinks. |
| 🚧 | Public Beta | Stable enough for most non-enterprise use-cases |
| ❌ | Public | Production-ready |

We are currently in: **Public Alpha**.

Wokrlcell is heavily under development, and we expect to iterate on the APIs/UIs before reaching beta (version 0.1.0).

## 🔖 Installation

- [Python](https://www.python.org/) version 3.8+

- Install Workcell using `pip`:

    ```bash
    pip install workcell
    ```

- Or using [Anaconda](http://anaconda.org/):

    ```bash
    conda install workcell
    ```

## 🚀 Quick Start

- After workcell installed, just run:

    ```bash
    workcell hello
    ```

- You can find an automatically generated [Swagger UI](https://github.com/swagger-api/swagger-ui) from `http://127.0.0.1:7860/docs`, then just goto `http://127.0.0.1:7860/ui` to try your first workcell app:) 

## 📚 Guide

- What happened? 

    Workcell has created a FastAPI service and a lightweight user interface for your functions without any additional API or UI-related code. This service is ready to be deployed to the cloud as a public service, requiring minimal setup on your end. 

- Speed up your development

    With Workcell, you can focus on developing your core functionality while leaving the infrastructure and deployment details to the platform. All you need is to make sure your function is **workcell compatible**.

- **Workcell compatible**

    A workcell-compatible function must have an `input` and `output` parameter and return value based on [Pydantic models](https://pydantic-docs.helpmanual.io/). The `input` and `output` are specified using [type hints](https://docs.python.org/3/library/typing.html).

    Here is an example of a simple **workcell compatible** function:

    ```python title=app.py
    from pydantic import BaseModel

    class Input(BaseModel):
        message: str

    class Output(BaseModel):
        message: str

    def hello_workcell(input: Input) -> Output:
        """Returns the `message` of the input data."""
        return Output(message=input.message)
    ```

## 🤗 Deployment

- Why deployment?

    You'll be able to access your workcell from anywhere and share it with your team and collaborators. Now you can deploy workcell to Hugging Face [Spaces](https://huggingface.co/spaces/launch) in 1-click! 

- **Prepare your Hugging Face account**

    First you need a Hugging Face account, and prepare a [User Access Tokens](https://huggingface.co/settings/tokens), then set environment variables like below:

    ```bash
    export HUGGINGFACE_USERNAME={huggingface_username}
    export HUGGINGFACE_TOKEN={huggingface_token}
    ```

    Replace `{huggingface_username}` and `{huggingface_token}` with yours.
    
    You can also store these environment variables in a `.env` file in your project folder for convenience.

- **Deploy in 1-click!**    

    Once you prepared a **workcell compatible** function (or project), just run:

    ```bash
    workcell up app:hello_workcell
    ```

    Voila! The deployment process will start, and within a few minutes, workcell will be available on your Hugging Face Spaces.

- **Extra explain**    

    When you run `workcell up`, there're actually 2 seperate step `workcell pack` and `workcell deploy` been applied. `workcell pack` will package your function code with a template into `.workcell` under your project folder, and `workcell deploy` will upload this folder to cloud.

## 📖 Documents

- You can find more details in our [documents](https://weanalyze.github.io/workcell/docs/quick-start).

## 🎮 Examples

- Get inspired and learn more about workcell by exploring our examples:
    -  https://github.com/weanalyze/workcell-examples

- We also have a curated list for you to check out, feel free to contribute!
    - https://github.com/weanalyze/best-of-workcell

## 🛣️ Roadmap

- Missing a feature? Have a look at our [public roadmap](https://github.com/orgs/weanalyze/projects/5/) to see what the team is working on in the short and medium term. Still missing it? Please let us know by opening an issue!

## 😆 Contacts

- If you have any questions about the workcell or weanalyze , feel free to email us at: support@weanalyze.co

- If you want to say hi, or are interested in partnering with us, feel free to reach us at: contact@weanalyze.co

- Feel free to share memes or any questions at Discord: https://discord.weanalyze.co

## License

Apache-2.0 License.
