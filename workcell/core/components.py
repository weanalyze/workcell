"""Contains all of the components that can be used with Workcell.
Along with the docs for each component, you can find the names of example demos that use
each component. These demos are located in the `examples` directory."""
from __future__ import annotations
from pydantic import BaseModel
from typing import Any


class Component(BaseModel):
    """
    A base class for defining the methods that all workcell components should have.
    """

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f"{self.get_component_name()}"

    def get_component_name(self) -> str:
        """
        Gets component's class name.

        If it is template component it gets the parent's class name.

        @return: class name
        """
        return (
            self.__class__.__base__.__name__.lower()
            if hasattr(self, "is_template")
            else self.__class__.__name__.lower()
        ) 

    def preprocess(self, x: Any) -> Any:
        """
        Any preprocessing needed to be performed on function input.
        """
        return x

    def postprocess(self, y):
        """
        Any postprocessing needed to be performed on function output.
        """
        return y

    def style(self, **kwargs):
        """
        This method can be used to change the appearance of the component.
        """        
        pass