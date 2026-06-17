from app.services.memory import query
from app.services.llm import get_llm_response
from app.services.memory_extractor import extract_memory
from app.services.memory import add

MATCH_SCORE_THRESHOLD=0.3

def respond(message:str):
    memory=extract_memory(message)
    # add message to the memory if it needs to be saved
    if memory['shouldSave']:
        del memory['shouldSave']
        add(memory);

    # process message as a query
    search_result=query(message)
    filtered_match=[result for result in search_result.points if result.score > MATCH_SCORE_THRESHOLD]
    memories = [search.payload['message'] for search in filtered_match]
    # if len(memories) < 1:
    #     return "I don't have relevant memory to answer this"
    response=get_llm_response(message,memories)
    return response