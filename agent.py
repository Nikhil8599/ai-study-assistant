from graph import build_graph

app = build_graph()

def ask(question, thread_id):
    state = {
        "question": question,
        "messages": [],
        "route": "",
        "retrieved": "",
        "sources": [],
        "tool_result": "",
        "answer": "",
        "faithfulness": 0.0,
        "eval_retries": 0
    }

    result = app.invoke(
        state,
        config={"configurable": {"thread_id": thread_id}}
    )

    return result["answer"]