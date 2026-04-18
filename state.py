from typing import TypedDict, List

class CapstoneState(TypedDict):
    question: str
    messages: List
    route: str
    retrieved: str
    sources: List
    tool_result: str
    answer: str
    faithfulness: float
    eval_retries: int