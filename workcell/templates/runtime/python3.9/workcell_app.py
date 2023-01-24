import os
import json
from workcell.core import Workcell
from workcell.api import create_api
from mangum import Mangum


# load workcell_config
with open("./workcell_config.json", "r") as f:
    workcell_config = json.load(f)
# load openapi prefix
openapi_prefix = "{}/{}".format(workcell_config['username'], workcell_config['workcell_name'])

# here's the magic
app = create_api(Workcell(workcell_config['workcell_entrypoint']))
app.root_path = openapi_prefix

# create lambda handler
handler = Mangum(app, api_gateway_base_path=openapi_prefix) # with openapi prefix behind proxy