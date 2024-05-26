# main.py
"""
This module demonstrates the integration and usage of various functionalities from the project.
It acts as an entry point for developers to understand how to utilize the modular components
to perform document processing, searching, and response generation.
"""

from apis.utils import init_pinecone, init_openai, init_tavily
from functions.document_processing import load_and_prepare_text
from functions.search_functions import init_pinecone, fetch_context_from_query
from functions.context_management import check_relevance_and_respond
from functions.response_generation import generate_response
from config.api_keys import PINECONE_API_KEY, OPENAI_API_KEY, TAVILY_API_KEY

def main():
    # Initialize APIs
    init_pinecone(PINECONE_API_KEY, "environment")
    tavily_client = init_tavily(TAVILY_API_KEY)
    init_openai(OPENAI_API_KEY)

    # Process and prepare documents
    texts = load_and_prepare_text("Your_File.txt")
    print("Texts prepared and loaded for indexing.")

    # Initialize document search capability
    docsearch = init_pinecone(PINECONE_API_KEY, "environment", "your index name")

    # Define the query
    query = "Elon Musk on renewable energy"
    
    # Fetch context using the document search
    context = fetch_context_from_query(docsearch, query)
    print("Context fetched from Pinecone search:", context)

    # Check context relevance
    relevance_response = check_relevance_and_respond(OPENAI_API_KEY, query, context)
    print(f"Is the fetched context relevant? {relevance_response}")

    # Fetch more detailed context from Tavily if initial context is not relevant
    if relevance_response == "No":
        print("Initial context did not contain the answer. Fetching more detailed context...")
        detailed_context = tavily_client.search(query=query, search_depth="advanced")
        print("Detailed context fetched from Tavily:", detailed_context)
        # Generate a response based on the detailed context
        response = generate_response(OPENAI_API_KEY, detailed_context)
    else:
        # Generate a response based on the initial context
        response = generate_response(OPENAI_API_KEY, context)

    print("Generated response:", response)

if __name__ == "__main__":
    main()
