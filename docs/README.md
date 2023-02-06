# Workcell CLI

**Usage**:

```console
$ [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `build`: Prepare deployment image for workcell.
* `deploy`: Deploy workcell.
* `export`: Package and export a workcell.
* `login`: Login into weanalyze.co.
* `new`: Init a new workcell template.
* `push`: Push image for workcell.
* `serve`: Start a HTTP API server for the workcell.
* `serve-ui`: Start a UI server for the workcell.
* `teardown`: Teardown a workcell on weanalyze cloud.
* `up`: Build->push->deploy a workcell to weanalyze...
* `version`: Return workcell version.

## `build`

Prepare deployment image for workcell.

This will create a deployment folder and build docker image. 

Args: 

    import_string (str): import_string, a.k.a workcell fqdn. 

        e.g. import_string = "app:hello_workcell" 

    image_tag (str): docker image tag. 

        e.g. image_tag = "weanalyze/hello_workcell:latest" 

        if set to default "", it will be "{username}/{workcell_name}:{workcell_version}" 

    workcell_version (str): workcell version. 

        e.g. workcell_version = "latest" 

    workcell_runtime (str): workcell runtime. 

        e.g. workcell_runtime = "python3.8" 

    workcell_tags (dict): workcell tags. 

        e.g. workcell_tags = '{"vendor":"aws", "service-type":"http"}' 

    workcell_env (dict): workcell env. 

        e.g. workcell_env = '{"STAGE":"latest"}' 

Return: 

    build_dir (str): project build directory. 

    workcell_config (dict): workcell configuration dict. 

**Usage**:

```console
$ build [OPTIONS] IMPORT_STRING
```

**Arguments**:

* `IMPORT_STRING`: [required]

**Options**:

* `-t, --image_tag TEXT`: [default: ]
* `-v, --version TEXT`: [default: latest]
* `-r, --runtime TEXT`: [default: python3.8]
* `--workcell_tags TEXT`: [default: {}]
* `--workcell_env TEXT`: [default: {}]
* `--help`: Show this message and exit.

## `deploy`

Deploy workcell.
This will deploy workcell by workcell_config.json in buidl_dir. Must be running in project folder or given build_dir.

Args: 

    build_dir (str): project build directory. 

Return: 

    None.

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

## `login`

Login into weanalyze.co.

Provide username and access_token to login into weanalyze.co.

**Usage**:

```console
$ login [OPTIONS]
```

**Options**:

* `-u, --username TEXT`: [default: ]
* `-a, --access_token TEXT`: [default: ]
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

* `-r, --runtime TEXT`: [default: python3.8]
* `--help`: Show this message and exit.

## `push`

Push image for workcell.
This will push image to repository based on workcell_config. Must be running in project folder or given build_dir.

Args: 

    build_dir (str): project build directory. 

Return: 

    None.

**Usage**:

```console
$ push [OPTIONS]
```

**Options**:

* `-b, --build_dir TEXT`: [default: .workcell]
* `--help`: Show this message and exit.

## `serve`

Start a HTTP API server for the workcell.

This will launch a FastAPI server based on the OpenAPI standard and with a automatic interactive documentation.

**Usage**:

```console
$ serve [OPTIONS] WORKCELL_PATH
```

**Arguments**:

* `WORKCELL_PATH`: [required]

**Options**:

* `-p, --port INTEGER`: [default: 3000]
* `-h, --host TEXT`: [default: 0.0.0.0]
* `--help`: Show this message and exit.

## `serve-ui`

Start a UI server for the workcell.

This will launch a Streamlit server based on the Pydantic standard.

**Usage**:

```console
$ serve-ui [OPTIONS] WORKCELL_PATH
```

**Arguments**:

* `WORKCELL_PATH`: [required]

**Options**:

* `-p, --port INTEGER`: [default: 3000]
* `-h, --host TEXT`: [default: 0.0.0.0]
* `--help`: Show this message and exit.

## `teardown`

Teardown a workcell on weanalyze cloud.

This will delete workcell infra on weanalyze cloud. Must be running in project folder or given build_dir.

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

This will create a deployment on weanalyze cloud. 

Args: 

    import_string (str): import_string, a.k.a workcell fqdn. 

        e.g. import_string = "app:hello_workcell" 

    image_tag (str): docker image tag. 

        e.g. image_tag = "weanalyze/hello_workcell:latest" 

        if set to default "", it will be "{username}/{workcell_name}:{workcell_version}" 

    workcell_version (str): workcell version. 

        e.g. workcell_version = "latest" 

    workcell_runtime (str): workcell runtime. 

        e.g. workcell_runtime = "python3.8" 

    workcell_tags (dict): workcell tags. 

        e.g. workcell_tags = '{"vendor":"aws", "service-type":"http"}' 

    workcell_env (dict): workcell env. 

        e.g. workcell_env = '{"STAGE":"latest"}' 

Return: 

    None.

**Usage**:

```console
$ up [OPTIONS] IMPORT_STRING
```

**Arguments**:

* `IMPORT_STRING`: [required]

**Options**:

* `-t, --image_tag TEXT`: [default: ]
* `-v, --version TEXT`: [default: latest]
* `-r, --runtime TEXT`: [default: python3.8]
* `--workcell-tags TEXT`: [default: {}]
* `--workcell-env TEXT`: [default: {}]
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

