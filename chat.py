
from user import User 
import re, ollama 
from ollama import ChatResponse
from transformers import pipeline



def parse_response(response: str) -> str:
    response = re.sub(r"<think>.*?</think>", "", response, flags=re.DOTALL).strip() 
    return response
    
class Chat:
    def __init__(
        self, 
        conver: str = 'deepseek-r1:1.5b',
        memory: str = 'deepseek-r1:1.5b', 
    ):
        self.conver = conver 
        self.memory = memory 
        self.history = []
        self.info = []
        
    def first(self, user: User) -> User:
        """First meeting with the chat-bot. The goal in the first conversation is 
        to get the NAME of the user and build the first MEMORY."""
        self.history.append({'role': 'system', 'content': f"You are a healthcare assistant. Do not give long answers or enumerations unless they are explicitly asked. You are talking to {user.NAME}. Let's start a conversation now."})
        while True:
            inp = input('You: ')
            if len(inp) == 0:
                break 
            response = self.send(inp, user)
            print(response)
        return self.close(user)
        
    def close(self, user: User) -> User:
        for m in user.MEMORY:
            self.info.append({f'role': 'assistant', 'content': m})
        self.info.append({'role': 'system', 'content': f'Give a summary of the emotional status of {user.NAME} in one paragraph. Now you should talk about {user.NAME}'})
        response = parse_response(ollama.chat(model=self.memory, messages=self.info).message.content)
        print('\n'+'-'*80 + '\n')
        print('Summary:\n')
        print(response)
        user.MEMORY.append(response)
        return user 
        
    def start(self, user: User) -> User:
        self.insert_diary(user)
        while True:
            inp = input('You: ')
            if len(inp) == 0:
                break 
            response = self.send(inp, user)
            print(response)
        return self.close(user)
                
    def send(self, message: str, user: User) -> str:
        # self.history.append({'role': 'system', 'content': "Do not give long answers or enumerations unless they are explicitly asked."})
        self.history.append({'role': 'user', 'content': message})
        if message.lower().startswith('thank') and len(message.split()) < 10:
            self.history.append({'role': 'assistant', 'content': "You're welcome! Let me know if there is something else I can help."})
            return self.history[-1]['content']
        self.info.append({'role': 'user', 'content': message})
        return self.get_answer(user)
    
    def get_answer(self, user: User) -> str:
        self.history.append({'role': 'system', 'content': f'Do not refer to {user.NAME} as a third person. YOU ARE ANSWERING {user.NAME}'})
        response: ChatResponse = ollama.chat(model=self.conver, messages=self.history, options={'temperature': 0.1, 'top_k': 10, 'mirostat_eta': 0.5})
        response = parse_response(response.message.content)
        self.history.pop(-1)
        self.history.append({'role': 'assistant', 'content': response})
        return response 
    
    def insert_diary(self, user: User):
        # sentiment analysis model
        sent = pipeline(model="lxyuan/distilbert-base-multilingual-cased-sentiments-student")
        emotions = sent(user.MEMORY)
        neg = [(i, record) for i, (em, record) in enumerate(zip(emotions, user.MEMORY)) if em['label'] == 'negative']
        pos  = [(i, record) for i, (em, record) in enumerate(zip(emotions, user.MEMORY)) if em['label'] == 'positive']
        self.history.append({'role': 'system', 'content': f"You are a healthcare assistant for {user.NAME}. "})
        if len(neg) > 0:
            self.history.append({'role': 'system', 'content': 
                             f'These are the negative things that happened to {user.NAME}. Do not mention them.\n' + \
                                 '\n'.join(f'Day {i+1}: {mem}' for i, mem in neg)})
        if len(pos) > 0:
            self.history.append({'role': 'system', 'content': 
                    f'These are the positive things that happened to {user.NAME}:\n' + \
                        '\n'.join(f'Day {i+1}: {mem}' for i, mem in neg)})
        self.history.append({'role':'system', 'content': f'Now you are talking to {user.NAME}. Do not give long answers or enumerations unless they are explicitly asked. ' +
                                 f"\nLet's start a conversation now. Start only with a greeting. Do not assume the emotional status."})
        
