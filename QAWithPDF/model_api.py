import os
from dotenv import load_dotenv
import sys

from llama_index.llms.gemini import Gemini
from IPython.display import display, Markdown
import google.generativeai as genai
from exception import CustomException
from logger import logging

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=GOOGLE_API_KEY)

def load_model():
    """
    Loads a Gemini model for natural language processing.

    Returns:
    - Gemini: An instance of the Gemini class initialized with the 'gemini-xxx' model.
    """

    try:
        model = Gemini(model="gemini-2.5-flash", api_key=GOOGLE_API_KEY)
        return model
    except Exception as e:
        raise CustomException(e, sys)