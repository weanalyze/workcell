from typing import Any, Dict
import streamlit as st

CUSTOM_STREAMLIT_CSS = """
div[data-testid="stBlock"] button {
  width: 100% !important;
  margin-bottom: 20px !important;
  border-color: #bfbfbf !important;
}
pre code {
    white-space: pre-wrap;
}
"""

class SessionState():
    def __init__(self, **kwargs: Any) -> None:
        """A new SessionState object."""
        self.session_state = st.session_state
        self.session_state._run_id = 0
        self.session_state._input_data: Dict = {}
        self.session_state._output_data: Any = None
        self.session_state._latest_operation_input: Any = None

        for key, val in kwargs.items():
            setattr(self, key, val)

    @property
    def run_id(self) -> int:
        return self.session_state._run_id

    @property
    def input_data(self) -> Dict:
        return self.session_state._input_data

    @property
    def output_data(self) -> Any:
        return self.session_state._output_data

    @output_data.setter
    def output_data(self, output_data: Any) -> None:
        self.session_state._output_data = output_data

    @property
    def latest_operation_input(self) -> Any:
        return self.session_state._latest_operation_input

    @latest_operation_input.setter
    def latest_operation_input(self, latest_operation_input: Any) -> None:
        self.session_state._latest_operation_input = latest_operation_input

    def clear(self) -> None:
        # Clear should higher the run ID to reset all widgets using this within their key
        self.session_state._run_id += 1
        self.session_state._input_data = {}
        self.session_state._output_data = None
        self.session_state._latest_operation_input = None


def get_session_state(**kwargs: Any) -> SessionState:
    """Gets a SessionState object for the current session.
    Creates a new object if necessary.
    """
    this_session = SessionState(**kwargs)
    return this_session