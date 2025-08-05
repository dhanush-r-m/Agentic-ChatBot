import streamlit as st
from src.Langraph.UI.Streamlit.load import LoadUI
from src.Langraph.LLMS.groqllm import GroqLLM
from src.Langraph.graph.graph_builder import GraphBuilder
from src.Langraph.UI.Streamlit.display_result import DisplayResult


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

    if user_message:
        try:
            obj_llm_config = GroqLLM(user_controls_input=user_input)
            model = obj_llm_config.get_llm_model()

            if not model:
                st.error("❌ Model configuration failed. Please check your inputs.")
                return

            usecase = user_input.get("usecase")

            if not usecase:
                st.error("❌ Use Case not selected. Please select a valid use case.")
                return
            
            graph_builder = GraphBuilder(model)
            try:
                graph = GraphBuilder(model).setup_graph("basic_chatbot")  # ✅ match naming
                DisplayResult("basic_chatbot", graph, user_input, debug=True).display_result_on_ui()

            except Exception as e:
                st.error(f"❌ Error setting up graph: {e}")
                return
        
        except Exception as e:
            st.error(f"❌ Error setting up graph: {e}")
            return
