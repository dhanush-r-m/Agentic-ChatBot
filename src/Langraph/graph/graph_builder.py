from langgraph.graph import StateGraph
from src.Langraph.state.state import State
from langgraph.graph import START, END



class GraphBuilder:
    """
    Custom GraphBuilder for Langraph.
    This class extends the base GraphBuilder to include additional functionality
    specific to the Langraph application.
    """

    def __init__(self, model):
        self.model = model
        self.graph_builder = StateGraph(State)

    def basic_build_chatbot_build(self):
        """
        Build a basic chatbot graph.
        This method initializes the graph with a simple structure suitable for a chatbot.
        """
        self.graph_builder.add_node("chatbot", "")
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_edge("chatbot" , END)
        
        return self.graph_builder