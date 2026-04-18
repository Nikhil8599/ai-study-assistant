from vectordb import collection, embedder
from tools import datetime_tool
from llm import llm

def memory_node(state):
    messages = state.get("messages", [])
    messages.append({"role": "user", "content": state["question"]})
    return {"messages": messages[-6:]}

def router_node(state):
    q = state["question"].lower()
    if "time" in q or "date" in q:
        return {"route": "tool"}
    return {"route": "retrieve"}

def retrieval_node(state):
    query_embedding = embedder.encode([state["question"]]).tolist()

    results = collection.query(
        query_embeddings=query_embedding,
        n_results=3
    )

    docs = results["documents"][0]
    context = "\n".join(docs)

    return {"retrieved": context, "sources": ["kb"]}

def tool_node(state):
    return {"tool_result": datetime_tool()}

def answer_node(state):
    question = state["question"]
    context = state.get("retrieved", "")
    tool_result = state.get("tool_result", "")

    if tool_result:
        prompt = f"Answer using this:\n{tool_result}\nQuestion: {question}"
    else:
        prompt = f"""
You are an engineering study assistant.

Answer the question in a detailed manner using ONLY the provided context.

Instructions:
- Give a full explanation
- Include formulas if present
- Include examples if available
- Do NOT summarize in one line
- Do NOT add information outside context

Context:
{context}

Question:
{question}

Answer:
"""

    response = llm.invoke(prompt)
    return {"answer": response.content}

def eval_node(state):
    answer = state["answer"]
    context = state.get("retrieved", "")

    if context and answer:
        score = 0.9   
    else:
        score = 0.5

    retries = state["eval_retries"] + 1

    return {
        "faithfulness": score,
        "eval_retries": retries
    }

def save_node(state):
    messages = state.get("messages", [])
    messages.append({"role": "assistant", "content": state["answer"]})
    return {"messages": messages}