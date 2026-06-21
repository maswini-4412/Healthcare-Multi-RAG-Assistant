from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document

from src.embeddings import get_embeddings

import pandas as pd
import json
import os


def create_indexes():

    embeddings=get_embeddings()


    # Medical RAG

    docs=[]

    for file in os.listdir("data/medical_pdfs"):

        path="data/medical_pdfs/"+file

        text=open(path,encoding="utf-8").read()

        docs.append(
            Document(
                page_content=text,
                metadata={"source":"medical"}
            )
        )


    db=FAISS.from_documents(
        docs,
        embeddings
    )

    db.save_local(
        "faiss_indexes/medical_index"
    )


    # Drug CSV RAG

    df=pd.read_csv(
        "data/drug_csv/medicines.csv"
    )

    drug_docs=[]

    for _,row in df.iterrows():

        drug_docs.append(

            Document(

            page_content=str(row.to_dict()),

            metadata={"source":"drug"}

            )
        )


    db=FAISS.from_documents(
        drug_docs,
        embeddings
    )


    db.save_local(
    "faiss_indexes/drug_index"
    )



    # Symptoms RAG


    data=json.load(
        open(
        "data/symptoms/symptoms.json"
        )
    )


    symptom_docs=[]


    for item in data:

        symptom_docs.append(

            Document(

            page_content=str(item),

            metadata={"source":"symptom"}

            )

        )


    db=FAISS.from_documents(
        symptom_docs,
        embeddings
    )


    db.save_local(
    "faiss_indexes/symptom_index"
    )



    # WHO RAG


    text=open(
    "data/who_guidelines/who_guidelines.txt",
    encoding="utf-8"
    ).read()


    db=FAISS.from_documents(

    [
    Document(
    page_content=text,
    metadata={"source":"who"}
    )
    ],

    embeddings

    )


    db.save_local(
    "faiss_indexes/who_index"
    )



if __name__=="__main__":

    create_indexes()

    print("FAISS indexes created successfully") 