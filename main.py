import streamlit as st
from document_processing.document_loader import FileProcessor
from text_cleaning.text_cleaner import TextPreprocessor
from database.vector_db import DBConnection
from text_chunking.text_chunker import TextChunker
from response_generation.response_generator import ResponseGenerator

# Initialize objects for each component
file_processor = FileProcessor()  # Handles file loading and text extraction
text_preprocessor = TextPreprocessor()  # Cleans and preprocesses the extracted text
db_connection = DBConnection()  # Connects to the Pinecone database for storage
text_chunker = TextChunker()  # Splits the text into manageable chunks
response_generator = ResponseGenerator()  # Handles generating responses based on user input

# Streamlit page configuration
st.set_page_config(
    page_title="RAG-Driven Document Q&A System",  # Set the page title
    page_icon="📄",  # Set the page icon
    layout="wide"  # Set the layout to wide for a better user experience
)

st.title("📄 RAG-Driven Document Q&A System")  # Display the main title on the page

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Document upload and processing section
with st.container():
    # File uploader to accept different document formats
    uploaded_file = st.file_uploader("Upload a document", type=["pdf", "txt", "docx"], help="Supported formats: PDF, TXT, DOCX")
    
    if uploaded_file:
        # Process the uploaded file and store the chunks in Pinecone
        file_text = file_processor.get_text(uploaded_file)  # Extract the text from the uploaded file
        cleaned_text = text_preprocessor.preprocess_text(file_text)  # Clean and preprocess the extracted text
        chunked_text = text_chunker.chunk_text(cleaned_text)  # Split the cleaned text into chunks
        db_connection.upload_to_pinecone(chunked_text, "attention")  # Upload the chunks to Pinecone

        # Confirmation message after successful file upload
        st.write("File uploaded successfully!") 

# Question and Answer section
with st.form(key="question_form"):
    st.header("💬 Ask a Question")  # Heading for the Q&A section
    user_input = st.text_input("Type your question here...")  # Text input for the user's question
    submit_button = st.form_submit_button("Submit")  # Submit button for the form
    
    if submit_button:
        # Generate the response using the input and current chat history
        response = response_generator.get_response(user_input, st.session_state.chat_history)

        # Update the session state chat history with user input and agent's response
        st.session_state.chat_history.append(("User", user_input))
        st.session_state.chat_history.append(("Agent", response))

        # Display the response
        st.write(f"🤖 Answer: {response}")

        # Display full chat history
        for role, message in st.session_state.chat_history:
            st.write(f"**{role}:** {message}")