import os

# Default lambda function role
WORKCELL_FOLDER = os.path.abspath(os.path.join(__file__ , "../.."))
TEMPLATE_FOLDER = os.path.join(WORKCELL_FOLDER, "templates")
SCAFFOLD_FOLDER = os.path.join(TEMPLATE_FOLDER, "scaffold")
RUNTIME_FOLDER = os.path.join(TEMPLATE_FOLDER, "runtime")


# Default workcell custom domain
WORKCELL_API_GATEWAY = "https://fun.weanalyze.co/api/v1"
WORKCELL_PORT = 7860
