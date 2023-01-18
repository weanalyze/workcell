from enum import Enum
from typing import Set
from pydantic import BaseModel, Field


class TextPreprocessingStep(str, Enum):
    REMOVE_SPECIAL_CHARACTERS = "remove-special-characters"
    REMOVE_SINGLE_CHARACTERS = "remove-single-characters"
    CLEAN_MULTIPLE_SPACES = "clean-multiple-spaces"
    LOWERCASE = "lowercase"
    REMOVE_STOP_WORDS = "remove-stop-words"


class TextPreprocessingInput(BaseModel):
    text: str
    preprocessing_steps: Set[TextPreprocessingStep] = Field(
        ..., description="Preprocessing steps to apply on the text."
    )

class TextPreprocessingOutput(BaseModel):
    preprocessed_text: str = Field(...)