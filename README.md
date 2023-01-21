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

Instantly turn your Python function into production-ready microservice, with lightweight UI to interact with. Use / Share / Publish / Collaborate with your team. 

<img align="center" style="width: 100%" src="https://github.com/weanalyze/weanalyze-resources/blob/main/assets/workcell_intro.png?raw=true"/>

---

## Highlights

- 🪄&nbsp; Turn functions into production-ready services within seconds.
- 🔌&nbsp; Auto-generated HTTP API based on FastAPI.
- 📦&nbsp; Deploy microservice into weanalye FaaS cloud.
- 🧩&nbsp; Reuse pre-defined templates & combine with existing components.
- 📈&nbsp; Instantly deploy and scale for production usage.

## Status

| Status | Stability | Goal |
| ------ | ------ | ---- |
| ✅ | Alpha | We are testing Workcell with a closed set of customers |
| 🚧 | Public Alpha | Anyone can sign up over at weanalyze.co. But go easy on us, there are a few kinks. |
| ❌ | Public Beta | Stable enough for most non-enterprise use-cases |
| ❌ | Public | Production-ready |

We are currently in Alpha. 

## Requirements

Python 3.8+

## Installation

Recomended: First activate your virtual environment, with your favourite system. For example, we like poetry and conda!

```bash
pip install workcell
```

## Getting Started

1. A simple workcell-compatible function could look like this:

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

    _💡 A workcell-compatible function is required to have an `input` parameter and return value based on [Pydantic models](https://pydantic-docs.helpmanual.io/). The input and output models are specified via [type hints](https://docs.python.org/3/library/typing.html)._

2. Copy this code to a file named `app.py`, put into a folder, e.g. `hello_workcell`

3. Run the HTTP API server from command-line:

    ```bash
    cd hello_workcell
    workcell serve app:hello_workcell
    ```
    _In the output, there's a line that shows where your API is being served, on your local machine._

4. Run the Streamlit based UI server from command-line:

    ```bash
    workcell serve-ui app:hello_workcell
    ```
    _In the output, there's a line that shows where your UI is being served, on your local machine._

5. **Deploy workcell into weanalyze cloud:**

   🚧 Working in progress, will be updated soon...

## Examples

💡 Find out more usage information and get inspired by our [examples](https://github.com/weanalyze/workcell/tree/main/examples).

## Roadmap

🗓️ Missing a feature? Have a look at our [public roadmap](https://github.com/orgs/weanalyze/projects/5/) to see what the team is working on in the short and medium term. Still missing it? Please let us know by opening an issue!

## Contacts

❓ If you have any questions about the workcell or weanalyze , feel free to email us at: support@weanalyze.co

🙋🏻 If you want to say hi, or are interested in partnering with us, feel free to reach us at: contact@weanalyze.co

😆 Feel free to share memes or any questions at Discord: https://discord.gg/jZuDU5mQZ7

## License

Apache-2.0 License.
