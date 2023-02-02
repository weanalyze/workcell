import json
import plotly
from pydantic import BaseModel, Field

from typing import TypeVar
PlotlyPlotType = TypeVar('plotly.graph_objects.Figure')


class PlotlyPlot(BaseModel):
    data: PlotlyPlotType = Field(
        ..., title="Plotly express fig", description="A plotly express fig encode in json format."
    )

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            plotly.graph_objects.Figure: lambda v: json.loads(v.to_json())
        }         