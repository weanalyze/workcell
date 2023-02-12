import os
import json
from workcell.core import Workcell, create_workcell_app


# load workcell_config
with open("./workcell_config.json", "r") as f:
    workcell_config = json.load(f)
    
# here's the magic
app = create_workcell_app(Workcell(workcell_config['workcell_entrypoint']))