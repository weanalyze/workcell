---
sidebar_position: 1
---

# Workcell CLI

**Usage**:

```console
$ [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `deploy`: Deploy workcell.
* `export`: Package and export a workcell.
* `hello`: Say hello to workcell.
* `new`: Init a new workcell template.
* `pack`: Prepare deployment image for workcell.
* `serve`: Start a HTTP API server for the workcell.
* `teardown`: Teardown workcell deployment.
* `up`: Build->push->deploy a workcell to weanalyze...
* `version`: Return workcell version.

## `deploy`

Deploy workcell.
This will deploy workcell by workcell.yaml in buidl_dir. Must be running in project folder or given build_dir.
Args: 

    provider (str): service provider, e.g. huggingface. 

    build_dir (str): project build directory. 

Return: 

    repo_url (str): huggingface repo url.

**Usage**:

```console
$ deploy [OPTIONS]
```

**Options**:

* `-b, --build_dir TEXT`: [default: .workcell]
* `--help`: Show this message and exit.

## `export`

Package and export a workcell.

**Usage**:

```console
$ export [OPTIONS] IMPORT_STRING
```

**Arguments**:

* `IMPORT_STRING`: [required]

**Options**:

* `--format [docker|we|pex|zip|pyz]`: [default: zip]
* `--help`: Show this message and exit.

## `hello`

Say hello to workcell.
This will create a `hello_workcell` project dir and serve it.

**Usage**:

```console
$ hello [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

## `new`

Init a new workcell template.
This will create a template dir for workcell deployment.

**Usage**:

```console
$ new [OPTIONS] PROJECT_NAME
```

**Arguments**:

* `PROJECT_NAME`: [required]

**Options**:

* `-p, --provider TEXT`: [default: huggingface]
* `-r, --runtime TEXT`: [default: python3.8]
* `--help`: Show this message and exit.

## `pack`

Prepare deployment image for workcell.
This will create a deployment folder and build docker image. 

Args: 

    import_string (str): import_string, a.k.a workcell entrypoint. 

        e.g. import_string = "app:hello_workcell" 

    workcell_provider (str): workcell provider. 

        e.g. workcell_provider = "huggingface" 
        
    workcell_version (str): workcell version. 

        e.g. workcell_version = "latest" 

    workcell_runtime (str): workcell runtime. 

        e.g. workcell_runtime = "python3.8" 

    workcell_tags (dict): workcell tags. 

        e.g. workcell_tags = '{"vendor":"aws", "service-type":"http"}' 

    workcell_envs (dict): workcell env. 

        e.g. workcell_envs = '{"STAGE":"latest"}' 

Return: 

    build_dir (str): project build directory. 

    workcell_config (dict): workcell configuration dict. 

**Usage**:

```console
$ pack [OPTIONS] IMPORT_STRING
```

**Arguments**:

* `IMPORT_STRING`: [required]

**Options**:

* `-p, --provider TEXT`: [default: huggingface]
* `-t, --image TEXT`: [default: ]
* `-v, --version TEXT`: [default: latest]
* `-r, --runtime TEXT`: [default: python3.8]
* `--workcell_tags TEXT`: [default: {}]
* `--workcell_envs TEXT`: [default: {}]
* `--help`: Show this message and exit.

## `serve`

Start a HTTP API server for the workcell.
This will launch a FastAPI server based on the OpenAPI standard and with a automatic interactive documentation.

**Usage**:

```console
$ serve [OPTIONS] WORKCELL_ENTRYPOINT
```

**Arguments**:

* `WORKCELL_ENTRYPOINT`: [required]

**Options**:

* `-c, --config PATH`
* `-p, --port INTEGER`: [default: 7860]
* `-h, --host TEXT`: [default: 127.0.0.1]
* `--help`: Show this message and exit.

## `teardown`

Teardown workcell deployment.
This will deploy workcell by workcell.yaml in buidl_dir. Must be running in project folder or given build_dir.
Args: 

    build_dir (str): project build directory. 

Return: 

    None.

**Usage**:

```console
$ teardown [OPTIONS]
```

**Options**:

* `-b, --build_dir TEXT`: [default: .workcell]
* `--help`: Show this message and exit.

## `up`

Build->push->deploy a workcell to weanalyze cloud.
This will create a deployment folder and build docker image. 

Args: 

    import_string (str): import_string, a.k.a workcell fqdn. 

        e.g. import_string = "app:hello_workcell" 

    workcell_provider (str): workcell provider. 

        e.g. workcell_provider = "huggingface" 
        
    workcell_version (str): workcell version. 

        e.g. workcell_version = "latest" 

    workcell_runtime (str): workcell runtime. 

        e.g. workcell_runtime = "python3.8" 

    workcell_tags (dict): workcell tags. 

        e.g. workcell_tags = '{"vendor":"aws", "service-type":"http"}' 

    workcell_envs(dict): workcell env. 

        e.g. workcell_envs = '{"STAGE":"latest"}' 

Return: 

    build_dir (str): project build directory. 

    workcell_config (dict): workcell configuration dict. 

**Usage**:

```console
$ up [OPTIONS] IMPORT_STRING
```

**Arguments**:

* `IMPORT_STRING`: [required]

**Options**:

* `-p, --provider TEXT`: [default: huggingface]
* `-v, --version TEXT`: [default: latest]
* `-r, --runtime TEXT`: [default: python3.8]
* `--workcell_tags TEXT`: [default: {}]
* `--workcell_envs TEXT`: [default: {}]
* `--help`: Show this message and exit.

## `version`

Return workcell version.
This will return the version of workcell package.

**Usage**:

```console
$ version [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

