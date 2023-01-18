import nltk
import re
from workcell.integrations.connectors import TextPreprocessingStep
from workcell.integrations.connectors import TextPreprocessingInput, TextPreprocessingOutput

try:
    EN_STOP_WORDS = set(nltk.corpus.stopwords.words("english"))
except LookupError:
    nltk.download("stopwords")
    EN_STOP_WORDS = set(nltk.corpus.stopwords.words("english"))


def preprocess_text(input: TextPreprocessingInput) -> TextPreprocessingOutput:
    """Clean up text data based on selected preprocessing steps."""

    text = input.text

    if TextPreprocessingStep.REMOVE_SPECIAL_CHARACTERS in input.preprocessing_steps:
        text = re.sub(r"\W", " ", text)

    if TextPreprocessingStep.REMOVE_SINGLE_CHARACTERS in input.preprocessing_steps:
        text = re.sub(r"\s+[a-zA-Z]\s+", " ", text)

    if TextPreprocessingStep.CLEAN_MULTIPLE_SPACES in input.preprocessing_steps:
        text = re.sub(r"\s+", " ", text, flags=re.I)

    if TextPreprocessingStep.LOWERCASE in input.preprocessing_steps:
        text = text.lower()

    if TextPreprocessingStep.REMOVE_STOP_WORDS in input.preprocessing_steps:
        tokens = text.split()
        tokens = [word for word in tokens if word not in EN_STOP_WORDS]
        text = " ".join(tokens)

    return TextPreprocessingOutput(preprocessed_text=text)
