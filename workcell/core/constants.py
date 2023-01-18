import os

# Default streamlit runner snippet
STREAMLIT_RUNNER_SNIPPET = """
from workcell.ui import render_streamlit_ui
from workcell.core import Workcell
from os import getcwd
import streamlit as st
st.set_page_config(page_title="Workcell", page_icon=":arrow_forward:")
with st.spinner("Loading Workcell. Please wait..."):
    workcell = Workcell("{workcell_path}")
render_streamlit_ui(workcell)
"""

# Default lambda function role
WORKCELL_FOLDER = os.path.abspath(os.path.join(__file__ , "../.."))
TEMPLATE_FOLDER = os.path.join(WORKCELL_FOLDER, "templates")
SCAFFOLD_FOLDER = os.path.join(TEMPLATE_FOLDER, "scaffold")
RUNTIME_FOLDER = os.path.join(TEMPLATE_FOLDER, "runtime")

# Default workcell custom domain
WORKCELL_CUSTOM_DOMAIN = "api.cell.weanalyze.co"
WORKCELL_API_GATEWAY = "https://fun.weanalyze.co/api/v1"
