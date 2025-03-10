import re

class TextPreprocessor:
    """
    Class for handling text cleaning and preprocessing.
    This class provides methods to clean, normalize, and preprocess text for further processing.
    """

    def __init__(self):
        """
        Initializes the TextPreprocessor.
        No arguments or attributes are required at initialization.
        """
        pass

    def clean_text(self, text):
        """
        Cleans the provided text by removing newline characters and extra spaces.
        
        Args:
            text (str): The text to be cleaned.
        
        Returns:
            str: The cleaned text with newline characters and extra spaces removed.
        """
        text = re.sub(r"\n", " ", text)  # Remove newline characters
        text = re.sub(r"\s+", " ", text).strip()  # Remove extra spaces and trim the text
        return text

    def remove_special_characters(self, text):
        """
        Removes special characters from the provided text, leaving only alphanumeric characters and spaces.
        
        Args:
            text (str): The text from which special characters are to be removed.
        
        Returns:
            str: The cleaned text with special characters removed.
        """
        return re.sub(r"[^a-zA-Z0-9\s]", "", text)  # Remove anything that's not a letter, number, or space

    def to_lower(self, text):
        """
        Converts all characters in the provided text to lowercase.
        
        Args:
            text (str): The text to be converted to lowercase.
        
        Returns:
            str: The lowercase version of the provided text.
        """
        return text.lower()  # Convert the text to lowercase

    def preprocess_text(self, text):
        """
        Preprocesses the provided text by applying all cleaning steps:
        - Removing newline characters
        - Removing special characters
        - Converting to lowercase
        
        Args:
            text (str): The text to be preprocessed.
        
        Returns:
            str: The fully preprocessed text.
        """
        text = self.clean_text(text)  # Clean text by removing newlines and extra spaces
        text = self.remove_special_characters(text)  # Remove special characters
        text = self.to_lower(text)  # Convert to lowercase
        return text


