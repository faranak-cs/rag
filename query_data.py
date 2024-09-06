import argparse
from langchain_chroma import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain_community.llms.ollama import Ollama

from get_embedding_function import get_embedding_function

CHROMA_PATH = "chroma"

PROMPT_TEMPLATE = """
Answer the question based only on the following context:

{context}

---

Answer the question based on the above context: {question}
"""


def main():
    parser = argparse.ArgumentParser(description='Talk to your documents using RAG')
    parser.add_argument("query_text", type=str, help="A query for the RAG")
    args = parser.parse_args()
    query_text = args.query_text
    query_rag(query_text)


def query_rag(query_text: str):

    # PREPARE CHROMA CLIENT
    embedding_function = get_embedding_function()
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)

    # SEARCH THE DATABASE
    results = db.similarity_search_with_score(query_text, k=1)
    # for doc, score in results:
    #     print(f"[SIM={score:3f}] {doc.page_content} [{doc.metadata}]")

    # PREPARE THE CONTEXT
    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    # print(context_text)

    # GENERATE PROMPT
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text)

    # SELECT MODEL
    model = Ollama(model="llama3.1")

    # GENERATE RESPONSE WITH SOURCES
    response_text = model.invoke(prompt)
    sources = [doc.metadata.get("id", None) for doc, _score in results]
    formatted_response = f"Response: {response_text}\nSources: {sources}"
    print(formatted_response)


if __name__ == "__main__":
    main()