from datetime import datetime

def datetime_tool():
    try:
        return f"Current date and time: {datetime.now()}"
    except Exception as e:
        return str(e)