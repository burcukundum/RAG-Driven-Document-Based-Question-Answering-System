from agents.agent_initializer import AgentSetup

class ResponseGenerator:
    """
    Class for generating responses using a pre-initialized agent.
    It utilizes the AgentSetup to configure and run the agent.
    """
    
    def __init__(self):
        """
        Initializes the ResponseGenerator by setting up the agent from AgentSetup.
        """
        self.agent = AgentSetup().get_agent()  # Get the pre-initialized agent from AgentSetup


    def get_response(self, user_input, chat_history):
        """Generate response based on user input and chat history."""

        # Run the agent with the user input and current chat history
        response = self.agent.run({"input": user_input, "chat_history": chat_history})
        self.agent.memory = chat_history

        return response


    










    
    
    
