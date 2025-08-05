import streamlit as st

class DisplayResult:
    """
    Class to handle the display of results in the Streamlit UI.
    It formats and displays the results based on the type of message received.
    """

    def __init__(self, usecase, graph, user_message):
        self.usecase = usecase
        self.graph = graph
        self.user_message = user_message
    
    def display_result_on_ui(self):
        # Show the user's message in the chat UI
        st.chat_message("user").write(self.user_message)

        # Prepare the input state for the LangGraph
        input_state = {"user_input": self.user_message}

        try:
            # Invoke the graph and get the final state
            final_state = self.graph.invoke(input_state)

            # Extract the chatbot's response
            response = final_state.get("response", "❌ No response returned from the chatbot.")

            # Show the assistant's response
            st.chat_message("assistant").write(response)

        except Exception as e:
            st.chat_message("assistant").write(f"❌ Error generating response: {e}")


             
