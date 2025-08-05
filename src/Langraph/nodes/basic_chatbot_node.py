from src.Langraph.state.state import State

class BasicChatbotNode:
    """
    A basic chatbot node that can be used in a Langraph workflow.
    This node is designed to handle simple chat interactions.
    """
    def __init__(self, model):
        self.llm = model

    def process(self, state: State) -> dict:
        """
        Process the input state and return a response.

        Args:
            state (State): The current state of the Langraph application.

        Returns:
            dict: A dictionary containing the response from the chatbot.
        """
        user_input = state.get("user_input", "")
        if not user_input:
            return {"response": "No user input provided."}

        response = self.llm.invoke(user_input)
        return {
            "user_input": user_input,
            "response": response
        }
