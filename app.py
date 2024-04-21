import os

import nltk
import requests
import streamlit as st
from nltk.tokenize import sent_tokenize

from responses import SubmitQuestionAndDocumentsResponse

try:
    _ = nltk.data.find("tokenizers/punkt")
except LookupError:
    nltk.download("punkt")

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass



st.set_page_config(layout="wide")

if os.getenv("ENV") == "production":
    BASE_URL = "https://deven-cleric-backend.onrender.com"
else:
    BASE_URL = "http://localhost:8000"


def make_sidebar():
    with st.sidebar:
        # st.title("Sidebar")
        # st.write("This is a sidebar.")
        # st.write("You can add widgets here")
        st.write("This functionality is not implemented yet, but it is a placeholder for future use.")
        st.write("It can be easily implemented to select the model to use for the question answering task.")
        _ = st.selectbox("Select the model", ["GPT-4", "Claude Opus"], disabled=True)


def create_payload(question, documents):
    documents = documents.split(",")
    payload = {"question": question, "documents": documents}
    return payload


def main():
    st.title("Deven's Cleric Assignment")
    # print("Hello, World!")
    make_sidebar()

    col1, col2 = st.columns([1,1])

    with col1:
        # st.write("This is column 1")
        documents = st.text_area(
            "Enter the URLs of the documents (separated by commas)",
            value="https://storage.googleapis.com/cleric-assignment-call-logs/call_log_20240314_104111.txt, \
                https://storage.googleapis.com/cleric-assignment-call-logs/call_log_20240315_104111.txt"
        )

    with col2:
        # st.write("This is column 2")
        question = st.text_input(
            "Ask the question", value="What product design decisions did the team make?"
        )

    payload = create_payload(question, documents)


    data = SubmitQuestionAndDocumentsResponse(**payload)
    # on = st.toggle('View model dump', False, key='view_model_dump')
    # if on:
    #     st.write(data.model_dump())

    if st.button("Submit"):
        # url = "https://deven-cleric-backend.onrender.com/submit_question_and_documents/"
        url = f"{BASE_URL}/submit_question_and_documents/"
        resp = requests.post(url, json=data.model_dump())
        # st.write(resp.status_code)
        # st.write(resp.json())

        url_local_get = f"{BASE_URL}/get_question_and_facts/"
        resp = requests.get(url_local_get)
        # st.write(resp.status_code)
        fact_str = ""
        if resp.status_code == 200:
            # st.write(resp.json())
            facts = resp.json()["facts"]
            st.write("Facts:")
            # st.write(len(facts), type(facts))
            # facts = sent_tokenize(facts)
            for i, fact in enumerate(facts):
                if len(fact) > 0:
                    fact = fact.replace("$", f"{chr(92)}$")
                    sentences = sent_tokenize(fact)
                    for sentence in sentences:
                        fact_str += f"""1. {sentence}\n"""

            st.markdown(fact_str)



if __name__ == "__main__":
    main()
