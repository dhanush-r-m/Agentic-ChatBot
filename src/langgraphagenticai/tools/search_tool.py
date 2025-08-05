from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import ToolNode


def get_tools():
    """
    Returns a list of tools for the chatbot.
    Currently, it includes a search tool using Tavily.
    """
    tools = [TavilySearchResults(max_results=2)]
    return tools

def create_tool_node(tools):
    """
    Creates a ToolNode for the chatbot.
    This node integrates the search tool into the chatbot's workflow.
    """

    return ToolNode(tools=tools)