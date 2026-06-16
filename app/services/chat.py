from app.services.memory import query
from app.services.llm import get_llm_response

def respond(message:str):
    search_result=query(message)
    filtered_match=[result for result in search_result.points if result.score > 0.5]
    memories = [search.payload['text'] for search in filtered_match]
    if len(memories) < 1:
        return "I don't have relevant memory to answer this"
    response=get_llm_response(message,memories)
    return response