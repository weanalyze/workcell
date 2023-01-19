<!-- markdownlint-disable MD033 MD041 -->
<h1 align="center">
    Workcell
</h1>

<p align="center">
    <strong>一键将Python函数转化成生产就绪的微服务.</strong>
</p>

<p align="center">
    <a href="https://pypi.org/project/workcell/" title="PyPi Version"><img src="https://img.shields.io/pypi/v/workcell?color=green&style=flat"></a>
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
        <a href="https://github.com/huggingface/transformers/">English</a> |
        <b>简体中文</b>
    <p>
</h4>

<p align="center">
  <a href="#getting-started">Getting Started</a> •
  <a href="#license">License</a> •
  <a href="https://github.com/weanalyze/workcell/releases">Changelog</a>
</p>

一键将Python函数转化成生产就绪的微服务, 并提供轻量的交互UI, 可以灵活使用/分享/发布/和团队协作. 

<img align="center" style="width: 100%" src="https://github.com/weanalyze/weanalyze-resources/blob/main/assets/workcell_intro.png?raw=true"/>

---

## 亮点

- 🪄&nbsp; 一键将函数转化成生产就绪的微服务.
- 🔌&nbsp; 基于FastAPI, 自动生成后端接口.
- 📦&nbsp; 将微服务部署到weanalyze云端.
- 🧩&nbsp; 复用模板, 共享工作空间, 实现更好的团队协作.
- 📈&nbsp; 快速部署并规模化以适应生产环境的需求.

## 状态

| 状态 | 产品阶段 | 目标 |
| ------ | ------ | ---- |
| ✅ | Alpha | 我们正在面向部分内测客户收集反馈意见, 并开源部分产品能力 |
| 🚧 | Public Alpha | 开源社区用户可以通过weanalyze.co注册账户, 并使用已实现的全部产品能力, 不过产品可能会有一些bug. |
| ❌ | Public Beta | 提升产品稳定性, 适用于大部分非商业用户场景. |
| ❌ | Public | 产品足够成熟, 适用于商业用户和生产环境. |

我们目前的阶段是: Alpha. 

## 需求

Python 3.8+

## 安装

建议: 使用你习惯的虚拟环境工具, 比如poetry和conda!

```bash
pip install workcell
```

## 开始使用

1. 一个可以部署为workcell的python函数:

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

    _💡 可以部署为workcell的python函数, 需要有一个 `input` 参数, 并返回一个 [Pydantic models](https://pydantic-docs.helpmanual.io/). 输入/输出的类格式可以参考 [type hints](https://docs.python.org/3/library/typing.html)._

2. 将这段代码拷贝到 `app.py` 中, 并 将`app.py`放置到一个文件夹中, 比如: `hello_workcell`

3. 一行代码运行后端服务:

    ```bash
    cd hello_workcell
    workcell serve app:hello_workcell
    ```
    _在命令行的输出中, 可以看到本地后端服务的地址_

4. 一行代码运行前端UI, 目前基于Streamlit实现:

    ```bash
    workcell serve-ui app:hello_workcell
    ```
    _在命令行的输出中, 可以看到本地UI服务的地址_

5. **一键将workcell部署到weanalyze云端:**

   🚧 完善中, 即将上线...

## 使用示例

💡 通过 [examples](https://github.com/weanalyze/workcell/tree/main/examples) 学习更多使用场景, 并获取灵感.

## 开发规划

🗓️ 感觉缺少一些必要的特性？可以看看我们的 [开发规划](https://github.com/orgs/weanalyze/projects/5/) 了解weanalyze团队短期、中期的开发规划. 如果有新特性的需求建议, 可以通过新建issues让我们了解!

## 联系我们

❓ 如果你在使用workcell的过程中遇到问题, 或任何与weanalyze.co产品使用相关的问题, 欢迎通过support邮箱联系我们: support@weanalyze.co

🙋🏻 如果你想和我们打个招呼, 或者对与我们沟通合作感兴趣, 欢迎通过contact邮箱联系我们: contact@weanalyze.co

😆 如果你想和开发团队以及开源社区爱好者分享你的见解和表情包, 欢迎加入discord社群: https://discord.gg/jZuDU5mQZ7

## 开源协议

Apache-2.0 License.
