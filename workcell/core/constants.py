import os

# Default file template
WORKCELL_FOLDER=os.path.abspath(os.path.join(__file__ , "../.."))
TEMPLATE_FOLDER=os.path.join(WORKCELL_FOLDER, "templates")
SCAFFOLD_FOLDER=os.path.join(TEMPLATE_FOLDER, "scaffold")
RUNTIME_FOLDER=os.path.join(TEMPLATE_FOLDER, "runtime")
# Default frontend template
WORKCELL_UI_TEMPLATE = os.path.join(TEMPLATE_FOLDER, "frontend", "index.html")

# Default workcell custom domain
WORKCELL_API_GATEWAY="https://fun.weanalyze.co/api/v1"
WORKCELL_API_SERVER="https://workcell.live/api/v1"
WORKCELL_SERVER_NAME="127.0.0.1"
WORKCELL_SERVER_PORT=7860
WORKCELL_NUM_PORTS=100