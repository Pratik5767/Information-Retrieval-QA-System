import google.generativeai as genai
from llama_index.llms.gemini import Gemini
from llama_index.core import VectorStoreIndex, Settings, load_index_from_storage
from llama_index.embeddings.gemini import GeminiEmbedding

from QAWithPDF.data_ingestion import load_data
from QAWithPDF.model_api import load_model

import sys
from exception import CustomException
from logger import logging


def download_gemini_embedding(model, document):
    """
    Downloads and initializes a Gemini Embedding model for vector embeddings.

    Returns:
    - VectorStoreIndex: An index of vector embeddings for efficient similarity queries.
    """

    try:
        logging.info("Initializing Gemini Embedding Model...")
        gemini_model_embedding = GeminiEmbedding(model_name="models/gemini-embedding-001")

        Settings.llm = model
        Settings.embed_model = gemini_model_embedding
        Settings.chunk_size = 800
        Settings.chunk_overlap = 20

        logging.info("Creating Vector Store Index from documents...")
        index = VectorStoreIndex.from_documents(document)
        index.storage_context.persist()

        logging.info("Query engine ready!")
        query_engine = index.as_query_engine()
        return query_engine
    except Exception as e:
        raise CustomException(e, sys)