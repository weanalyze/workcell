from __future__ import annotations
import time
from typing import Callable

from workcell.core.workcell import Workcell
from workcell.core.routes import create_workcell_app
from workcell.core.networking import start_server


def create_app(fn: Callable | str):
    workcell = Workcell(fn)
    app = create_workcell_app(workcell)
    return app


def launch_app(fn: Callable | str, port: int, host: str) -> None:
    import uvicorn
    workcell = Workcell(fn)
    app = create_workcell_app(workcell)
    uvicorn.run(app, host=host, port=port, log_level="info")


def launch_app_socket(workcell_path: str, port: int, host: str) -> None:
    workcell = Workcell(workcell_path)
    server_name, server_port, local_url, app, server = start_server(workcell, server_name=host, server_port=port)
    try:
        while True:
            time.sleep(0.1)
    except (KeyboardInterrupt, OSError):
        print("Keyboard interruption in main thread... closing server.")
        server.close()

