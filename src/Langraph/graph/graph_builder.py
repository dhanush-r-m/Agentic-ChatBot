from langgraph.graph import StateGraph
from src.Langraph.state.state import State
from langgraph.graph import START, END
from src.Langraph.nodes.basic_chatbot_node import BasicChatbotNode



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

        self.basic_chatbot_node = BasicChatbotNode(self.llm)


        self.graph_builder.add_node("chatbot", "self.basic_chatbot_node.process")
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_edge("chatbot" , END)
        
    
    def setup_graph(self , usecase:str):
        """
        Setup the graph based on the selected use case.
        This method configures the graph structure according to the specified use case.
        """
        
        if usecase == "basic_chatbot":
            self.basic_build_chatbot_build()