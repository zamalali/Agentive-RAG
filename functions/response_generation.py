# response_generation.py
import openai

def summarize_context(search_results, api_key):
    context = ' '.join([f"{item['content']} See more: {item['url']}" for item in search_results])
    prompt = f"Summarize the following information into a concise answer: {context}"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "You are a summarization assistant."},
                  {"role": "user", "content": prompt}],
        max_tokens=150,
        api_key=api_key
    )
    content = response['choices'][0]['message']['content'].strip()
    return content
