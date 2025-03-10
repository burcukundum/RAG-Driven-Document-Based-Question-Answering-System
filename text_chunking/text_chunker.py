from langchain.text_splitter import RecursiveCharacterTextSplitter

class TextChunker:
    """
    Class for splitting text into smaller chunks for processing.
    Useful for breaking large text documents into manageable pieces for models or further processing.
    """

    def __init__(self, chunk_size=500, chunk_overlap=100):
        """
        Initializes the TextChunker with specified chunk size and overlap.
        
        Args:
            chunk_size (int): The maximum size of each text chunk (default: 500).
            chunk_overlap (int): The number of overlapping characters between chunks (default: 100).
        """
        self.chunk_size = chunk_size  # Set the chunk size
        self.chunk_overlap = chunk_overlap  # Set the chunk overlap

    def chunk_text(self, text):
        """
        Splits the provided text into smaller chunks.
        
        Args:
            text (str): The text to be split into chunks.
        
        Returns:
            list: A list of text chunks.
        """
        # Initialize the text splitter with the specified chunk size and overlap
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size,  
            chunk_overlap=self.chunk_overlap,  
            length_function=len  
        )
        
        # Split the text into chunks
        chunks = splitter.split_text(text)
        return chunks  # Return the list of chunks
