# context_management.py
import openai
from .search_functions import fetch_context_from_query

def check_relevance_and_respond(query, context, api_key):
    system_message = f"""
    System:
    You are a security checker tasked with verifying whether the provided text contains a direct answer to the user's question. Respond only with 'Yes' or 'No'.
    Context provided: {context}
    Question: {query}
    """
    conversation = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": query}
    ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation,
        max_tokens=5,  
        api_key=api_key
    )
    content = response['choices'][0]['message']['content'].strip()
    return content