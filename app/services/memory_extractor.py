import requests
import json

LLM_URL="http://localhost:11434/api/generate"

def extract_memory(message:str):
    payload = {
        "model": "llama3",
        "prompt": f"""
            You are a memory extraction system.

            Determine if the message contains long-term information worth remembering.

            Message needs to be saved if it is:
            1. a personal information or fact.
            2. an identity information
            3. occupation or education information
            4. long-term goals
            5. skills and expertise
            6. relationships
            7. recurring habits
            8. stable interest

            Do NOT save if:
            1. Questions
            2. Temporary requests
            3. Small talks
            4. Greetings
            5. One-time activities
            6. Information that is already implied in the conversation
            7. Time-sensitive information unless its a long-term fact

            Categories:
            The memory categories could be:
            1. personal_information
            2. identity
            3. preferences
            4. relationships
            5. skills
            6. goals
            7. others

            Respond only in the below mentioned JSON format(Return ONLY valid JSON.). No additional text:
            {{
                category: Assign a category (name) to the memory from the "Categories" mentioned above,
                importance: A number from 0 to 1 based on how important a piece of memory seems to be,
                message: Message to save as memory,
                shouldSave: true or false
            }}

            Examples:

            Input:
            I like pizza

            Output:
            {{
                shouldSave: true,
                message: User like pizza
            }}

            You need to process the below input:

            Input:
            {message}

            """,
        "stream": False
    }
    response = requests.post(LLM_URL,json=payload)
    response_text=response.json()['response']
    return json.loads(response_text)