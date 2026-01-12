import os 
from dotenv import load_dotenv 

load_dotenv()

class Config:
    ASTRA_DB_API_ENDPOINT = os.getenv('ASTRA_DB_API_ENDPOINT')
    ASTRA_DB_APPLICATION_TOKEN = os.getenv('ASTRA_DB_APPLICATION_TOKEN')
    ASTRA_DB_KEYSPACE = os.getenv('ASTRA_DB_KEYSPACE')
    ASTRA_DB_COLLECTION_NAME = os.getenv('ASTRA_DB_COLLECTION_NAME')
    HUGGINGFACE_HUB_API = os.getenv('HUGGINGFACE_HUB_API')

    RAG_MODEL = os.getenv('MODEL_NAME')
    GROQ_API_KEY = os.getenv('GROQ_API_KEY')
    EMBEDDING_MODEL = "BAAI/bge-base-en-v1.5"


# config = Config()
    