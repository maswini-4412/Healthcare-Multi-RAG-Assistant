import streamlit as st

from src.rag_chain import ask_question



st.set_page_config(

page_title="Healthcare Multi RAG Assistant"

)



st.title(
"Healthcare Multi-RAG Assistant"
)


question = st.text_input(

"Ask healthcare question"

)


if st.button("Ask"):


    if question:


        result = ask_question(question)


        st.write(
        "RAG Selected:",
        result["rag_used"]
        )


        st.write(
        result["answer"]
        ) 