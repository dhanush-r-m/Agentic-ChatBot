from typing_extensions import TypedDict
from langgraph.graph.message import add_messages
from typing import Annotated



class State(TypedDict):
    """
    State for Langraph application.
    This state is used to manage the application's data and configuration.
    """
    messages: Annotated[list[str], add_messages]