import plotly
import jsonpickle
from pydantic import BaseModel, Field

from typing import TypeVar
PlotlyFigureType = TypeVar('plotly.graph_objects.Figure')


class PlotlyExpressPlot(BaseModel):
    data: PlotlyFigureType = Field(
        ..., title="Plotly express fig", description="A plotly express fig encode in json format."
    )

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            plotly.graph_objects.Figure: lambda v: v.to_json()
        }         