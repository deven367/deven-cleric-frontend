import requests
import streamlit as st

from responses import SubmitQuestionAndDocumentsResponse

st.set_page_config(layout="wide")

def make_sidebar():
    with st.sidebar:
        st.title("Sidebar")
        st.write("This is a sidebar.")
        st.write("You can add widgets here")

def create_payload(question, logs):
    payload = {
        "question": question,
        "logs": logs
    }
    # st.write(payload)
    return payload

def process_payload(payload):
    all_logs = payload["logs"]
    text = ""
    for log in all_logs:
        text += requests.get(log).text

    payload['text'] = text
    return payload

def main():
    st.title("Hello, World!")
    # print("Hello, World!")
    make_sidebar()

    col1, col2 = st.columns(2)

    with col1:
        st.write("This is column 2")
        logs = st.multiselect("Select the options",
                              [
                                  "https://storage.googleapis.com/cleric-assignment-call-logs/call_log_20240314_104111.txt",
                                  "https://storage.googleapis.com/cleric-assignment-call-logs/call_log_20240315_104111.txt",
                                  "https://storage.googleapis.com/cleric-assignment-call-logs/call_log_20240316_104111.txt",])

    with col2:
        st.write("This is column 1")
        question = st.text_input("Ask the question", value="What product design decisions did the team make?")

    payload = create_payload(question, logs)
    processed_payload = process_payload(payload)
    # st.write(processed_payload)

    data = SubmitQuestionAndDocumentsResponse(**processed_payload)
    st.write(data.model_dump())

    if st.button("Submit"):
        url = "https://deven-cleric-backend.onrender.com/submit_question_and_documents/"
        url_local = "http://
        resp = requests.post(url, json=data.model_dump())
        st.write(resp.status_code)
        st.write(resp.json())

if __name__ == "__main__":
    main()