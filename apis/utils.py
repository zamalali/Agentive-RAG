# apis/api_utils.py
import pinecone
from tavily import TavilyClient
import openai

def init_pinecone(api_key, environment):
    """Initialize the Pinecone environment with the given API key and environment details."""
    pinecone.init(api_key=api_key, environment=environment)

def init_tavily(api_key):
    """Create and return a Tavily client using the provided API key."""
    return TavilyClient(api_key=api_key)

def init_openai(api_key):
    """Set the OpenAI API key for future API calls."""
    openai.api_key = api_key
