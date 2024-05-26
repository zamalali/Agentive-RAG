# search_functions.py
import pinecone
from langchain.vectorstores import Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain

def init_pinecone(api_key, environment, index_name):
    pinecone.init(api_key=api_key, environment=environment)
    docsearch = Pinecone.from_texts(texts=" ", embedding=embeddings, index_name=index_name)
    return docsearch

def fetch_context_from_query(docsearch, query):
    docs = docsearch.similarity_search(query)
    llm = OpenAI(model="gpt-3.5-turbo-instruct", temperature=0, openai_api_key=userdata.get('OPENAI_API_KEY'))
    chain = load_qa_chain(llm, chain_type="stuff")
    context = chain.run(input_documents=docs, question=query)
    return context
