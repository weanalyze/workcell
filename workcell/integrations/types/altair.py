import json
import altair
from pydantic import BaseModel, Field
# from typing import Dict


from typing import TypeVar
AltairPlotType = TypeVar('altair.vegalite.v4.api.Chart')
# AltairPlotType = Dict

class AltairPlot(BaseModel):
    data: AltairPlotType = Field(
        ..., title="Altair vegalite v4 chart", description="A altair vegalite v4 chart type, will be exported in json format."
    )

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            altair.vegalite.v4.api.Chart: lambda v: json.loads(v.to_json()),
            altair.vegalite.v4.api.LayerChart: lambda v: json.loads(v.to_json())
        } 