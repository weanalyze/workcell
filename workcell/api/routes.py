import os
import json
import orjson
import mimetypes
import markupsafe

from typing import Any, Dict, Optional
import fastapi
from fastapi import status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from fastapi.responses import (
    HTMLResponse,
    JSONResponse,
)
from starlette.responses import RedirectResponse

from workcell import __ui_version__ as workcell_ui_version
from workcell.core import Workcell
from workcell.core.constants import (
    TEMPLATE_FOLDER,
    WORKCELL_PORT
)
from workcell.core.documentation import document, set_documentation_group
from workcell.core.errors import (
    TemplateNotFoundError,
)
# from workcell.api.utils import patch_fastapi


class ORJSONResponse(JSONResponse):
    media_type = "application/json"

    @staticmethod
    def _render(content: Any) -> bytes:
        return orjson.dumps(
            content,
            option=orjson.OPT_SERIALIZE_NUMPY | orjson.OPT_PASSTHROUGH_DATETIME,
            default=str,
        )

    def render(self, content: Any) -> bytes:
        return ORJSONResponse._render(content)

    @staticmethod
    def _render_str(content: Any) -> str:
        return ORJSONResponse._render(content).decode("utf-8")


def toorjson(value):
    return markupsafe.Markup(
        ORJSONResponse._render_str(value)
        .replace("<", "\\u003c")
        .replace(">", "\\u003e")
        .replace("&", "\\u0026")
        .replace("'", "\\u0027")
    )


mimetypes.init()
templates = Jinja2Templates(directory=TEMPLATE_FOLDER)
templates.env.filters["toorjson"] = toorjson


class App(fastapi.FastAPI):
    """
    FastAPI App Wrapper
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def configure_app(self, workcell: Workcell) -> None:
        self.workcell = workcell
        return None

    def update_app(self, 
        workcell_url: Optional[str]=None, 
        workcell_host: Optional[str]="0.0.0.0",
        workcell_port: Optional[int]=7860,
        workcell_style: Optional[str]="dark",
    ) -> None:
        self.workcell_host = workcell_host
        self.workcell_port = workcell_port
        self.workcell_url = workcell_url
        self.workcell_style = workcell_style
        return None

    def get_workcell(self) -> Workcell:
        if self.workcell is None:
            raise ValueError("No Workcell has been configured for this app.")
        return self.workcell

    def get_workcell_config(self) -> Dict:
        if self.workcell is None:
            raise ValueError("No Workcell has been configured for this app.")
        # workcell_config = self.workcell.config
        workcell_config = {}
        if self.workcell_url:
            workcell_url = self.workcell_url
        else:
            workcell_url = "http://" + str(self.workcell_host) + ":" + str(self.workcell_port)
        workcell_config['workcell_url'] = workcell_url
        return workcell_config


def create_app(workcell: Workcell) -> App:
    app = App(
        title=workcell.name, 
        version=workcell.config['workcell_version'], 
        description=workcell.description,             
        default_response_class=ORJSONResponse
    )
    app.configure_app(workcell)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
    )

    ###############
    # Main Routes
    ###############

    # Redirect to docs
    @app.get(
        "/", 
        include_in_schema=False
    )
    def root() -> Any:
        return RedirectResponse("./docs")

    # UI
    @app.get("/ui", response_class=HTMLResponse)
    def ui(request: fastapi.Request):
        mimetypes.add_type("application/javascript", ".js")
        config = app.get_workcell_config()
        try:
            template ="frontend/index.html"
            return templates.TemplateResponse(
                template, {"request": request, "config": config}
            )
        except Exception:
            raise TemplateNotFoundError(
                "Did you install Workcell from source files? Workcell ui only "
                "works when Workcell is installed through the pip package."
            )

    # API 
    @app.post(
        "/call",
        operation_id="call",
        response_model=workcell.output_type,
        # response_model_exclude_unset=True,
        summary="Execute the workcell.",
        status_code=status.HTTP_200_OK,
    )
    def call(input: workcell.input_type) -> Any:  # type: ignore
        """Executes this workcell."""
        return workcell(input)

    @app.get(
        "/info",
        operation_id="info",
        response_model=Dict,
        summary="Get info metadata.",
        status_code=status.HTTP_200_OK,
    )
    def info() -> Any:  # type: ignore
        """Returns informational metadata about this Workcell."""
        return {"info":workcell.description}

    @app.get(
        "/spec",
        operation_id="spec",
        response_model=Dict,
        # response_model_exclude_unset=True,
        summary="Get workcell spec.",
        status_code=status.HTTP_200_OK,
    )
    def spec() -> Any:  # type: ignore
        """Returns informational metadata about this Workcell."""
        return {"spec":workcell.spec}

    return app


def launch_app(workcell_path: str, port: int = WORKCELL_PORT, host: str = "0.0.0.0") -> None:
    import uvicorn
    workcell_app = create_app(Workcell(workcell_path))
    workcell_app.update_app(workcell_host=host, workcell_port=port)
    uvicorn.run(workcell_app, host=host, port=port, log_level="info")


def mount_workcell_app(
    app: fastapi.FastAPI,
    workcell: Workcell,
    path: str,
    workcell_api_url: Optional[str] = None,
) -> fastapi.FastAPI:
    """Mount a Workcell to an existing FastAPI application.

    Parameters:
        app: The parent FastAPI application.
        workcell: The Workcell object we want to mount to the parent app.
        path: The path at which the workcell application will be mounted.
        workcell_api_url: The full url at which the workcell app will run. This is only needed if deploying to Huggingface spaces of if the websocket endpoints of your deployed app are on a different network location than the workcell app. If deploying to spaces, set workcell_api_url to 'http://localhost:7860/'
    Example:
        from fastapi import FastAPI
        import workcell
        app = FastAPI()
        @app.get("/")
        def read_main():
            return {"message": "This is your main app"}
        workcell_app = ""
        app = workcell.mount_gradio_app(app, workcell_app, path="/workcell")
        # Then run `uvicorn run:app` from the terminal and navigate to http://localhost:8000/workcell.
    """
    workcell_app = App.create_app(workcell)
    app.mount(path, workcell_app)
    return app
