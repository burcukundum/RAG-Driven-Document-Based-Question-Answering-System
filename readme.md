
# RAG-Driven Document-Based Question Answering System

This project implements an AI-powered system capable of answering user queries based on the contents of uploaded PDF documents. The system utilizes various components such as document loading, chunking, cleaning, and a question-answering agent to provide accurate answers using context from the documents.

## Project Structure

The project is organized into the following directory structure:

```
.
├── agents
│   └── agent_initializer.py                # Initializes and configures the agent
├── database
│   └── vector_db.py                       # Handles Pinecone connection, embedding, and document retrieval
├── document_processing
│   └── document_loader.py                 # Extracts text from PDF files
├── response_generation
│   └── response_generator.py              # Generates responses using the pre-configured agent
├── text_chunking
│   └── text_chunker.py                    # Splits text into smaller chunks
├── text_cleaning
│   └── text_cleaner.py                    # Cleans and preprocesses text
├── requirements.txt                       # Project dependencies
├── .env                                   # Environment variables (Google API, Pinecone API keys)
└── README.md                              # Project documentation
```

### 1. **agents**
Contains the agent setup and initialization code that configures the conversational agent.

- **`agent_initializer.py`**: Initializes and configures the agent using LangChain and Google Gemini AI.

### 2. **database**
Handles the connection to Pinecone, manages embeddings, and handles document storage and retrieval.

- **`vector_db.py`**: Manages the connection to Pinecone, generates embeddings using SentenceTransformer, and handles document retrieval.

### 3. **document_processing**
Responsible for processing uploaded documents and extracting text content, particularly from PDF files.

- **`document_loader.py`**: Contains methods for extracting text from PDF files.

### 4. **response_generation**
Generates responses based on the user's query and document context.

- **`response_generator.py`**: Uses a pre-configured agent to generate responses to user input.

### 5. **text_chunking**
Splits large text documents into smaller, manageable chunks for processing.

- **`text_chunker.py`**: Contains logic for splitting text into smaller chunks using `RecursiveCharacterTextSplitter`.

### 6. **text_cleaning**
Cleans and preprocesses text to make it ready for further processing and model inference.

- **`text_cleaner.py`**: Provides methods to clean, normalize, and preprocess text, such as removing special characters and converting to lowercase.

## Installation

To get started with the project, clone this repository and install the required dependencies:

```bash
git clone https://github.com/burcukundum/RAG-Driven-Document-Based-Question-Answering-System.git
cd RAG-Driven-Document-Based-Question-Answering-System
pip install -r requirements.txt
```

Ensure you have the necessary API keys and environment variables set up. Create a `.env` file with the following content:

```
GOOGLE_API_KEY=your_google_api_key
PINECONE_API_KEY=your_pinecone_api_key
```

## Usage

1. **Document Upload**: Upload a PDF document to the system.
2. **Text Processing**: The document's text is extracted, cleaned, and split into chunks.
3. **Database Storage**: The chunks are embedded and stored in Pinecone for fast retrieval.
4. **Query**: Ask the agent questions related to the document.
5. **Response Generation**: The system retrieves the most relevant document excerpts and generates accurate answers.
6. **Run the app using Streamlit**:
```bash
streamlit run main.py
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
