"""
Defines helper methods useful for setting up ports, launching servers, and
creating tunnels.
"""
from __future__ import annotations

import os
import socket
import threading
import time
import warnings
from typing import Tuple
from typing import TYPE_CHECKING, Tuple

import requests
import uvicorn
from workcell.core.workcell import Workcell
from workcell.core.routes import App, create_workcell_app

# By default, the local server will try to open on localhost, port 7860.
# If that is not available, then it will try 7861, 7862, ... 7959.
INITIAL_PORT_VALUE = int(os.getenv("WORKCELL_SERVER_PORT", "7860"))
TRY_NUM_PORTS = int(os.getenv("WORKCELL_NUM_PORTS", "100"))
LOCALHOST_NAME = os.getenv("WORKCELL_SERVER_NAME", "127.0.0.1")


class Server(uvicorn.Server):
    def install_signal_handlers(self):
        pass

    def run_in_thread(self):
        self.thread = threading.Thread(target=self.run, daemon=True)
        self.thread.start()
        while not self.started:
            time.sleep(1e-3)

    def close(self):
        self.should_exit = True
        self.thread.join()


def configure_app(app: App, workcell: Workcell) -> App:
    auth = workcell.auth
    if auth is not None:
        if not callable(auth):
            app.auth = {account[0]: account[1] for account in auth}
        else:
            app.auth = auth
    else:
        app.auth = None
    app.workcell = workcell
    app.cwd = os.getcwd()
    app.favicon_path = workcell.favicon_path
    app.tokens = {}
    return app


def get_first_available_port(initial: int, final: int) -> int:
    """
    Gets the first open port in a specified range of port numbers
    Parameters:
    initial: the initial value in the range of port numbers
    final: final (exclusive) value in the range of port numbers, should be greater than `initial`
    Returns:
    port: the first open port in the range
    """
    for port in range(initial, final):
        try:
            s = socket.socket()  # create a socket object
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind((LOCALHOST_NAME, port))  # Bind to the port
            s.close()
            return port
        except OSError:
            pass
    raise OSError(
        "All ports from {} to {} are in use. Please close a port.".format(
            initial, final - 1
        )
    )


def url_ok(url: str) -> bool:
    try:
        for _ in range(5):
            with warnings.catch_warnings():
                warnings.filterwarnings("ignore")
                r = requests.head(url, timeout=3, verify=False)
            if r.status_code in (200, 401, 302):  # 401 or 302 if auth is set
                return True
            time.sleep(0.500)
    except (ConnectionError, requests.exceptions.ConnectionError):
        return False
    return False


def start_server(
    workcell: Workcell,
    server_name: str | None = None,
    server_port: int | None = None,
    ssl_keyfile: str | None = None,
    ssl_certfile: str | None = None,
    ssl_keyfile_password: str | None = None,
) -> Tuple[str, int, str, App, Server]:
    """Launches a local server running the provided Interface
    Parameters:
    workcell: The Blocks object to run on the server
    server_name: to make app accessible on local network, set this to "0.0.0.0". Can be set by environment variable GRADIO_SERVER_NAME.
    server_port: will start gradio app on this port (if available). Can be set by environment variable GRADIO_SERVER_PORT.
    auth: If provided, username and password (or list of username-password tuples) required to access the Blocks. Can also provide function that takes username and password and returns True if valid login.
    ssl_keyfile: If a path to a file is provided, will use this as the private key file to create a local server running on https.
    ssl_certfile: If a path to a file is provided, will use this as the signed certificate for https. Needs to be provided if ssl_keyfile is provided.
    ssl_keyfile_password: If a password is provided, will use this with the ssl certificate for https.
    Returns:
    port: the port number the server is running on
    path_to_local_server: the complete address that the local server can be accessed at
    app: the FastAPI app object
    server: the server object that is a subclass of uvicorn.Server (used to close the server)
    """
    server_name = server_name or LOCALHOST_NAME
    # if port is not specified, search for first available port
    if server_port is None:
        port = get_first_available_port(
            INITIAL_PORT_VALUE, INITIAL_PORT_VALUE + TRY_NUM_PORTS
        )
    else:
        try:
            s = socket.socket()
            s.bind((LOCALHOST_NAME, server_port))
            s.close()
        except OSError:
            raise OSError(
                "Port {} is in use. If a gradio.Blocks is running on the port, you can close() it or gradio.close_all().".format(
                    server_port
                )
            )
        port = server_port

    url_host_name = "localhost" if server_name == "0.0.0.0" else server_name

    if ssl_keyfile is not None:
        if ssl_certfile is None:
            raise ValueError(
                "ssl_certfile must be provided if ssl_keyfile is provided."
            )
        path_to_local_server = "https://{}:{}/".format(url_host_name, port)
    else:
        path_to_local_server = "http://{}:{}/".format(url_host_name, port)
    
    app = create_workcell_app(workcell)

    if workcell.save_to is not None:  # Used for selenium tests
        workcell.save_to["port"] = port
        
    config = uvicorn.Config(
        app=app,
        port=port,
        host=server_name,
        log_level="info",
        ssl_keyfile=ssl_keyfile,
        ssl_certfile=ssl_certfile,
        ssl_keyfile_password=ssl_keyfile_password,
        ws_max_size=1024 * 1024 * 1024,  # Setting max websocket size to be 1 GB
    )
    server = Server(config=config)
    server.run_in_thread()
    return server_name, port, path_to_local_server, app, server
