import streamlit as st

from src.Langraph.UI.Streamlit.load import LoadUI

def load_langgraph_agenticai_app():
    """
    Load the LangGraph Agentic AI application using Streamlit.
    This function initializes the UI , handles user input, configures the LLM Model,
    sets up the graph based on the selected use case, and manages the session state.



    """

    ## Load UI
    ui = LoadUI()
    user_input = ui.load_streamlit_ui()

    if not user_input:
        st.warning("⚠️ Please select an LLM and Use Case to proceed.")
        return
    
    user_message = st.chat_input("Enter your message here:", key="user_message")

    