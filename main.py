import requests
import json


OLLAMA_URL = "http://localhost:11434/api/generate"


def req_llm(prompt):
    prompt = f"""You are a helpful study assistant.Generate Clear, Simple, Beginner-friendly Responses.Follow the instructions given in the prompt carefully.
    
    {prompt} 
     """
    response = requests.post(
        OLLAMA_URL,
        json={
                "model" : "mistral",
                "prompt" : prompt,
                "stream" : False,
                "temperature": 0.3
        }
    )
    return response.json()["response"]


def check_intent(prompt):
    prompt = f""" 
    Classify the user input into ONE or MORE of these intents ONLY:
    - qna
    - generate_notes
    - save_notes
    

    Return ONLY JSON NO extra text before or after:
    {{
       "intent": ["intent1","intent2"]
    }}
    - Strictly return response in JSON format only  
    - DO NOT invent new values
    - NO extra text
    - NO explanation
    - Output must start with{{ and end with }}
    - Do not write anything else
    {prompt}
    """
    return req_llm(prompt)
    

    # notes_keywords = ["notes","make notes","create notes","generate notes","summarize","summary","explain in points","short notes"]
    # save_keywords = ["save","save notes","store","save this"]

    
    # is_save = any(word in user_input for word in save_keywords)
    # is_notes = any(word in user_input for word in notes_keywords)

    # if is_save and is_notes:
    #     return "save_and_generate"

    # elif is_save:
    #     return "save_notes"

    # elif is_notes:
    #     return "generate_notes"

    # return "do nothing"


def notes_generator(prompt):
    prompt = f"""
    Give clear, structured notes with:
  - Topic
  - Definition
  - Key Points
  - Example
    Return only JSON:{{
    "topic" : "...",
    "definition" : "...",
    "key_points" : ["...","..."],
    "example" : "..."
    }}
    DO NOT REPEAT SAME LINES IN THE NOTES.
    {prompt}
    """
    return req_llm(prompt)
    
    
def save_notes(topic,latest):
    #save the notes
    filename = f"{topic}.txt"
    with open(filename,"w") as file:
       file.write(json.dumps(latest, indent=2))
    print("Notes created Successfully.")


def unsafe_query(input):
    unsafe_keywords = ["suicide","kill","hack","cheat", "steal", "theft", "fraud", "scam", "blackmail",
    "forge", "piracy", "illegal","attack", "bomb", "weapon", "poison",
    "murder", "assault"]

    is_not_safe = any(word in input for word in unsafe_keywords)
    
    if is_not_safe:
        return "BLOCK"
    else:
        return "SAFE"


notes = []
while True:
    user_input  = input("Enter you input : ").strip()
    if not user_input:
        continue
    user_input = user_input.lower()

    #to quit the chat
    if user_input == "exit":
        break
    
    intent_result = check_intent(user_input)
    intents = None
    try:
        parsed = json.loads(intent_result)
        if isinstance(parsed, dict):
           intents = parsed.get("intent")
        elif isinstance(parsed, list):
           intents = parsed
        
    except Exception as e:
        print("Error parsing intent")
        print("RAW RESPONSE:", intent_result)   
        continue
    
    query = unsafe_query(user_input)
    
    
     #to handle unsafe queries
    if query == "BLOCK":
        print("Try asking something safe or educational.")
        continue
   
    if "generate_notes" in intents:
        notes_gen_result = notes_generator(user_input)
        print(notes_gen_result)
        try: 
            parsed_ = json.loads(notes_gen_result)
        except:
            print("Error parsing notes")
            continue
        notes.append(parsed_)
        
    if "save_notes" in intents: 
        if not notes:
            print("Notes never generated")
        else :
            latest = notes[-1]
            save_notes(latest["topic"], latest)

    if "qna" in intents: 
        result = req_llm(user_input)
        print(result)


  
    



















