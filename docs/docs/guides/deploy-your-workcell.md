---
sidebar_position: 4
---

# Deploy your workcell

You can deploy your workcell to [Hugging Face Spaces](https://huggingface.co/spaces) in 1-click! You'll be able to access your workcell from anywhere and share it with your team and collaborators.

## Prepare a Hugging Face account

First you need a [Hugging Face](http://huggingface.co/) account, and prepare your `Username` and `User Access Token`.

Set environment variables like below:

```bash
export HUGGINGFACE_USERNAME={huggingface_username}
export HUGGINGFACE_TOKEN={huggingface_token}
```

Replace `{huggingface_username}` with your actual Hugging Face `Username`, and `{huggingface_token}` with your actual `User Access Token` (format like `hf_xxx`). 

You can also store these environment variables in a `.env` file in your project folder for convenience.

## Deploy your workcell to Hugging Face

1. Wrap your function with `workcell.create_app` like example above

2. In your project folder, package your workcell app using the following command:

```bash
workcell pack app:hello_workcell
```

:::tip
`pack` command will package your function with a `Dockerfile` template into `.workcell` folder in your project folder.
:::

Once packaged, deploy your workcell app using the following command:

```bash
workcell deploy
```

🤗 Voila! The deployment process will start, and within a few minutes, your workcell will be available on Hugging Face Spaces, accessible by a unique URL.

## Workcell management

- You can monitor the deployment process and the logs in your terminal, and the deployment status will be shown in your Hugging Face Spaces repo.

- You can deploy multiple workcells, and they will be listed in your [Hugging Face Spaces](https://huggingface.co/spaces) account, you can manage them from there.

- You can also configure various deployment options like environment variables, system requirements, custom domain, etc., by using command line options or a `workcell.yaml` from `.workcell` dir in your project folder.

## More details

You can check **[workcell-cli docs](../documents/workcell-cli)** for more details. 
