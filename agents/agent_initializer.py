from langchain.agents import initialize_agent, Tool, AgentType
from langchain_google_genai import ChatGoogleGenerativeAI
from database.vector_db import DBConnection
from langchain.prompts import PromptTemplate
from langchain.agents import initialize_agent
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Define the prompt template for the agent, including input and context for document-based answers
AGENT_PROMPT_TEMPLATE = PromptTemplate(
    input_variables=["input", "context"],
    template="""  
You are an AI assistant that answers user questions based on retrieved documents (PDF).
Use the provided document context to generate accurate answers.

---
**User Question:** {input}

**Relevant Document Excerpt:**  
{context}

---
**Instructions:**  
- Answer using only the given context.  
- If the answer is **not found**, say: *"I couldn't find relevant information in the document."*  
- Format responses clearly, using bullet points if necessary.  

**Your Answer:**
"""
)

class AgentSetup:
    """
    Class to initialize and configure the agent for document retrieval and question answering.
    """

    def __init__(self):
        """
        Initialize the AgentSetup by setting up the LLM model, database connection, and agent.
        """
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-2.0-flash", 
            google_api_key=os.getenv("GOOGLE_API_KEY")
        )  # Initialize the LLM model with Google API key
        self.db_connection = DBConnection()  # Initialize the database connection
        self.memory = None
        self._create_agent()  # Set up the agent after initialization

    def _create_agent(self):
        """
        Create and configure the agent for conversational document retrieval and QA.
        """

        self.agent = initialize_agent(
            tools=[self._get_retrieval_tool()],
            llm=self.llm,
            agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
            verbose=True,
            memory=self.memory,
            agent_kwargs={"prompt": AGENT_PROMPT_TEMPLATE}  # Use the predefined structured prompt
        )

    def _get_retrieval_tool(self):
        """
        Create and return the tool used to retrieve documents from the database.
        This tool is responsible for fetching relevant document excerpts based on the query.
        """
        return Tool(
            name="Document Retriever",
            func=self.db_connection.get_similar_documents,
            description="Retrieves documents related to the query."
        )
    
    
    def get_agent(self):
        """
        Return the initialized agent for use in question-answering tasks.
        """
        return self.agent




