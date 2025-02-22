from user import User, List 
from chat import parse_response
import ollama, re 

ENNEAGRAM = ['Type 1: The Perfectionist', 'Type 2: The Giver', 'Type 3: The Achiever',
             'Type 4: The Individualist', 'Type 5: The Investigator', 'Type 6: The Skeptic',
             'Type 7: The Enthusiast', 'Type 8: The Challenger', 'Type 9: The Peacemaker']
MBTI = ['ISTJ: The Inspector', 'ISTP: The Crafter', 'ISFJ: The Protector', 'ISFP: The Artist',
        'INFJ: The Advocate', 'INFP: The Mediator', 'INTJ: The Architect', 'INTP: The Thinker',
        'ESTP: The Persuader', 'ESTJ: The Director', 'ESFP: The Performer', 'ESFJ: The Caregiver',
        'ENFP: The Champion', 'ENFJ: The Giver', 'ENTP: The Debater', 'ENTJ: The Commander']

class Profiler:
    def __init__(self, pretrained: str = 'deepseek-r1:7b', model: str = 'Enneagram', types: List[str] = ENNEAGRAM):
        self.model = model 
        self.types = types 
        self.pretrained = pretrained 
        self.history = []
        
    def user_view(self, user: User) -> User:
        self.history.append({'role': 'system', 'content': f'You are a personality profiler based on the {self.model} test. '})
        self.history.append({'role': 'system', 'content': 
                             f'These are the latest records of {user.NAME}:\n' + '\n'.join(f'Day {i+1}: {mem}' for i, mem in enumerate(user.MEMORY)) + \
                                 f"\nMake an analysis about which personality type is {user.NAME}. Do not write more than two paragraphs." })
        user.PERSONALITY = self.get_answer()
        return user 
    
    def stats(self, user: User) -> User:
        if not self.model in user.STATS.keys():
            user.STATS[self.model] = dict()
        for typ in self.types:
            value = None 
            while value is None:
                self.history.append({'role': 'system', 'content': f'You are a personality profiler based on the {self.model} test. '})
                self.history.append({'role': 'system', 'content': 
                                    f'These are the latest records of {user.NAME}:\n' + '\n'.join(f'Day {i+1}: {mem}' for i, mem in enumerate(user.MEMORY)) + \
                                        f'Give me the probability of {user.NAME} being {typ}. Only answer a number with % (e.g. 20%).'})
                answer = self.get_answer()
                if len(re.findall(r'\d{1,3}%', answer)) > 0:
                    value = int(re.findall(r'\d{1,3}%', answer)[0].replace('%', ''))
                    break 
            user.STATS[self.model][typ] = value 
            self.history = []
        return user
                
    def get_answer(self) -> str:
        response = parse_response(ollama.chat(model=self.pretrained, messages=self.history).message.content)
        self.history.append({'role': 'assistant', 'content': response})
        return response 
    