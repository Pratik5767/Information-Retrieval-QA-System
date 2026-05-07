import google.generativeai as genai
from llama_index.llms.gemini import Gemini
from llama_index.core import VectorStoreIndex, Settings, load_index_from_storage
from llama_index.embeddings.gemini import GeminiEmbedding

from QAWithPDF.data_ingestion import load_data
from QAWithPDF.model_api import load_model

import sys
from exception import CustomException
from logger import logging


def download_genai_embedding(model, document):
    """
    Downloads and initializes a Gemini Embedding model for vector embeddings.

    Returns:
    - VectorStoreIndex: An index of vector embeddings for efficient similarity queries.
    """

    try:
        pass
    except Exception as e:
        raise CustomException(e, sys)