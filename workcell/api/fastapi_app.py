from typing import Any, Dict

from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse

from workcell.core import Workcell
from workcell.api.fastapi_utils import patch_fastapi


def launch_api(workcell_path: str, port: int = 8501, host: str = "0.0.0.0") -> None:
    import uvicorn

    from workcell.core import Workcell
    from workcell.api import create_api

    app = create_api(Workcell(workcell_path))
    uvicorn.run(app, host=host, port=port, log_level="info")
    

def create_api(workcell: Workcell) -> FastAPI:

    title = workcell.name
    if "workcell" not in workcell.name.lower():
        title += " - workcell"
    
    app = FastAPI(
        title=title, 
        version=workcell.version, 
        description=workcell.description, 
    )

    patch_fastapi(app)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    # Redirect to docs
    @app.get("/", include_in_schema=False)
    def root() -> Any:
        return RedirectResponse("./docs")

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
        # response_model_exclude_unset=True,
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
