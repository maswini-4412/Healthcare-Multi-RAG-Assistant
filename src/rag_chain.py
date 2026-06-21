from src.router import route_question

from src.retrievers import load_retrievers

from src.llm import get_llm



retrievers = load_retrievers()

llm = get_llm()



def ask_question(question):


    rag_type = route_question(question)


    retriever = retrievers[rag_type]


    docs = retriever.invoke(question)


    context = ""


    for doc in docs:

        context += doc.page_content + "\n"



    prompt=f"""

You are a healthcare assistant.

Use only the below context.

Context:

{context}


Question:

{question}


Answer:

"""


    response = llm.invoke(prompt)


    return {

        "rag_used": rag_type,

        "answer": response.content
    } 
