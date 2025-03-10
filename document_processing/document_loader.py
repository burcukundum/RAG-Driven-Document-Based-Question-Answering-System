from PyPDF2 import PdfReader

class FileProcessor:
    """
    Class for processing uploaded files and extracting text content from PDF files.
    Currently, it only supports PDF file processing.
    """
    
    def extract_pdf_text(self, uploaded_file):
        """
        Extracts text from an uploaded PDF file.
        
        Args:
            uploaded_file (byte object): The PDF file as a byte object.
        
        Returns:
            str: The extracted text from the PDF file.
        """
        reader = PdfReader(uploaded_file)  # Create a PdfReader object to read the PDF
        text = ""
        for page_num in range(len(reader.pages)):  # Iterate through each page in the PDF
            page = reader.pages[page_num]
            text += page.extract_text()  # Extract the text from the current page
        return text  # Return the concatenated text from all pages

    def get_text(self, uploaded_file):
        """
        Extracts text from the provided file. Currently, only PDF files are supported.
        
        Args:
            uploaded_file (byte object): The uploaded file as a byte object.
        
        Returns:
            str: The extracted text from the file.
        """
        return self.extract_pdf_text(uploaded_file)  # Call extract_pdf_text for PDF files
