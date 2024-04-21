import os

import requests
import streamlit as st

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass


from responses import SubmitQuestionAndDocumentsResponse

st.set_page_config(layout="wide")

if os.getenv("ENV") == "production":
    BASE_URL = "https://deven-cleric-backend.onrender.com"
else:
    BASE_URL = "http://localhost:8000"


def make_sidebar():
    with st.sidebar:
        st.title("Sidebar")
        st.write("This is a sidebar.")
        st.write("You can add widgets here")

def create_payload(question, documents):
    payload = {"question": question, "documents": documents}
    return payload


def main():
    st.title("Hello, World!")
    # print("Hello, World!")
    make_sidebar()

    col1, col2 = st.columns(2)

    with col1:
        st.write("This is column 1")
        documents = st.multiselect(
            "Select the options",
            [
                "https://storage.googleapis.com/cleric-assignment-call-logs/call_log_20240314_104111.txt",
                "https://storage.googleapis.com/cleric-assignment-call-logs/call_log_20240315_104111.txt",
                "https://storage.googleapis.com/cleric-assignment-call-logs/call_log_20240316_104111.txt",
            ],
        )

    with col2:
        st.write("This is column 2")
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
        st.write(resp.json())


if __name__ == "__main__":
    main()
