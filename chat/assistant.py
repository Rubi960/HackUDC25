
import re, ollama 
from transformers import pipeline
from typing import List, Dict
from .models import History, User


def parse_response(response: str) -> str:
    response = re.sub(r"<think>.*?</think>", "", response, flags=re.DOTALL).strip() 
    return response
    
class Assistant:
    def __init__(self, user: User, conver: str = 'deepseek-r1:32b', memory: str = 'deepseek-r1:32b'):
        """Initialization of the AI assistant.

        Args:
            user (User): Input current user.
            conver (str): Conversational model for responses. Defaults to 'deepseek-r1:32b'.
            memory (str): Memory model for summarization. Defaults to 'deepseek-r1:32b'.
        """
        self.user = user 
        self.conver = conver 
        self.memory = memory 
        
        if len(self.user_memory) == 0:
            self.first_meeting()
        else:
            self.insert_diary()
            
    @property
    def user_memory(self) -> List[str]:
        if 'session_set' not in self.user.__dict__.keys():
            return []
        return list(self.user.session_set.all())
    
    def add_history(self, new: Dict[str, str]):
        h = History.objects.get(user=self.user)
        h.append(new)
        h.save()
        
    @property
    def history(self) -> List[Dict[str, str]]:
        return History.objects.get(user=self.user).history    
    @property
    def info(self) -> List[Dict[str, str]]:
        return [m for m in self.history if m['role'] == 'user']
    
    def remove_history(self, index: int):
        h = History.objects.get(user=self.user)
        h.history.pop(index)
        h.save()
            
    def first_meeting(self):
        """Introduce initial information of an user."""
        self.add_history({'role': 'system', 'content': 
            f"You are a healthcare assistant. Do not give long answers or enumerations unless they are explicitly asked. You are talking to {self.user.first_name}. Let's start a conversation now."})
        
    def insert_diary(self):
        """Introduces the past records of the user."""
        # sentiment analysis model
        sent = pipeline(model="lxyuan/distilbert-base-multilingual-cased-sentiments-student")
        emotions = sent(self.user_memory)
        neg = [(i, record) for i, (em, record) in enumerate(zip(emotions, self.user_memory)) if em['label'] == 'negative']
        pos  = [(i, record) for i, (em, record) in enumerate(zip(emotions, self.user_memory)) if em['label'] == 'positive']
        self.add_history({'role': 'system', 'content': f"You are a healthcare assistant for {self.user.first_name}. "})
        if len(neg) > 0:
            self.add_history({'role': 'system', 'content': 
                             f'These are the negative things that happened to {self.user.first_name}. Do not mention them.\n' + \
                                 '\n'.join(f'Day {i+1}: {mem}' for i, mem in neg)})
        if len(pos) > 0:
            self.add_history({'role': 'system', 'content': 
                    f'These are the positive things that happened to {self.user.first_name}:\n' + \
                        '\n'.join(f'Day {i+1}: {mem}' for i, mem in neg)})
        self.add_history({'role':'system', 'content': f'Now you are talking to {self.user.first_name}. Give short answers. No enumerations unless they are explicitly asked. ' +
                                 f"\nLet's start a conversation now. Start only with a greeting. Do not assume the emotional status."})
        
    def answer(self, message: str) -> str:
        """Updates the chat of the assistant with a new message and the assistant's response.

        Args:
            message (str): New message from the user.

        Returns:
            str: Assistant response.
        """
        self.add_history({'role': 'user', 'content': message})
        
        # analyze if the user is thanking
        if message.lower().startswith('thank') and len(message.split()) < 10:
            self.add_history({'role': 'assistant', 'content': "You're welcome! Let me know if there is something else I can help."})
            return self.history[-1]['content']
        
        # force the model to answer
        # self.history.append({'role': 'system', 'content': "Do not give long answers or enumerations unless they are explicitly asked."})
        self.add_history({'role': 'system', 'content': f'Do not refer to {self.user.first_name} as a third person. YOU ARE ANSWERING {self.user.first_name}'})
        response = parse_response(ollama.chat(model=self.conver, messages=self.history, options={'temperature': 0.1, 'top_k': 10, 'mirostat_eta': 0.5}).message.content)
        self.remove_history(-1) # remove the system prompt
        self.add_history({'role': 'assistant', 'content': response})
        return response 

    def summary(self) -> str:
        """Returns the summary of the assistant session."""
        info = self.info
        for m in self.user_memory:
            info.append({f'role': 'assistant', 'content': m})
        info.append({'role': 'system', 'content': f'Give a summary of the emotional status of {self.user.first_name} in one paragraph. Now you should talk about {self.user.first_name}'})
        response = parse_response(ollama.chat(model=self.memory, messages=info).message.content)
        return response  
    
