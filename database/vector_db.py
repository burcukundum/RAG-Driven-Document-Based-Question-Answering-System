import pinecone 
import os
from sentence_transformers import SentenceTransformer
import numpy as np
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()


class DBConnection:
    """
    Class to handle the connection to Pinecone, generate embeddings, and manage document storage/retrieval.
    """

    def __init__(self):
        """
        Initialize the dbConnection by setting up Pinecone, the SentenceTransformer model,
        and the Pinecone index.
        """
        # Initialize Pinecone with API key
        self.pc = pinecone.Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
        self.index_name = "quickstart"  # Name of the Pinecone index
        self.model = SentenceTransformer("all-MiniLM-L6-v2")  # Load the SentenceTransformer model
        self.index = self._create_index()  # Create or retrieve the Pinecone index

    def _create_index(self):
        """
        Creates a new Pinecone index if it doesn't already exist.
        Uses cosine similarity as the metric and AWS serverless cloud configuration.
        """
        if self.index_name not in self.pc.list_indexes().names():
            self.pc.create_index(
                name=self.index_name,
                dimension=384,  # Dimensions based on the model
                metric="cosine",  # Metric for similarity calculation
                spec=pinecone.ServerlessSpec(
                    cloud="aws",
                    region="us-east-1"
                ) 
            )
        return self.pc.Index(self.index_name)  # Return the Pinecone index object

    def get_embedding(self, text):
        """
        Generates an embedding for the given text using a pre-trained SentenceTransformer model.
        """
        return self.model.encode(text).tolist()  # Return the embedding as a list

    def upload_to_pinecone(self, chunked_text, doc_id):
        """
        Uploads chunked text and its corresponding embeddings to the Pinecone index.
        
        Args:
            chunked_text (list): A list of text chunks to be uploaded.
            doc_id (str): A unique identifier for the document.
        """
        vectors = []  # List to store vector information
        for id, text in enumerate(chunked_text):
            embedding = self.get_embedding(text)  # Get the embedding for the text chunk

            vectors.append({
                "id": doc_id + str(id),  # Unique ID for each chunk
                "values": embedding,  # The embedding values
                "metadata": {"text": text}  # Metadata containing the text
            })
        
        self.index.upsert(vectors)  # Upload the vectors to Pinecone

    def get_similar_documents(self, query_text, num_results=4):
        """
        Retrieves the most similar documents to the query text from Pinecone.
        
        Args:
            query_text (str): The query text to search for.
            num_results (int): The number of similar documents to return (default is 4).
        
        Returns:
            list: A list of similar document texts.
        """
        query_embedding = self.get_embedding(query_text)  # Get the embedding for the query
        results = self.index.query(vector=[query_embedding], top_k=num_results, include_metadata=True)  # Query Pinecone
        
        # Extract and return the relevant documents
        documents = [match["metadata"]["text"] for match in results["matches"]]
        
        return documents  # Return the list of similar documents
