import streamlit as st
from QAWithPDF.data_ingestion import load_data
from QAWithPDF.embedding import download_gemini_embedding
from QAWithPDF.model_api import load_model


def main():
    # setting application config
    st.set_page_config("QA with Documents")

    # used for uploading the file
    doc = st.file_uploader("Upload your document")

    # header of the project
    st.header("QA with document(Information Retrieval)")

    # here user will ask questions to model
    user_question = st.text_input("Ask your question")

    # logic for response / submit button
    if st.button("Submit & Response"):
        
        # spinner
        with st.spinner("Processing...."):
            document = load_data(doc)
            model = load_model()
            query_engine = download_gemini_embedding(model, document)

            response = query_engine.query(user_question)
            st.write(response.response)


if __name__=='__main__':
    main()