import os

# Default file template
WORKCELL_FOLDER=os.path.abspath(os.path.join(__file__ , "../.."))
TEMPLATE_FOLDER=os.path.join(WORKCELL_FOLDER, "templates")
SCAFFOLD_FOLDER=os.path.join(TEMPLATE_FOLDER, "scaffold")
RUNTIME_FOLDER=os.path.join(TEMPLATE_FOLDER, "runtime")
# Default frontend template
WORKCELL_UI_MANIFEST = "https://api.weanalyze.co/storage/v1/object/public/manifests/workcell_ui_manifest.json"
WORKCELL_UI_TEMPLATE = os.path.join(TEMPLATE_FOLDER, "frontend", "index.html")

# Supported Providers
SUPPORT_PROVIDER = ["huggingface", "weanalyze"]
SUPPORT_RUNTIME = ["python3.8", "python3.9"]

# Default workcell custom domain
WORKCELL_SERVER_NAME="127.0.0.1"
WORKCELL_SERVER_PORT=7860
WORKCELL_NUM_PORTS=100