from typing import Dict, List 
from chat.assistant import parse_response
import ollama, re 

ENNEAGRAM = ['Type 1: The Perfectionist', 'Type 2: The Giver', 'Type 3: The Achiever',
             'Type 4: The Individualist', 'Type 5: The Investigator', 'Type 6: The Skeptic',
             'Type 7: The Enthusiast', 'Type 8: The Challenger', 'Type 9: The Peacemaker']
MBTI = ['ISTJ: The Inspector', 'ISTP: The Crafter', 'ISFJ: The Protector', 'ISFP: The Artist',
        'INFJ: The Advocate', 'INFP: The Mediator', 'INTJ: The Architect', 'INTP: The Thinker',
        'ESTP: The Persuader', 'ESTJ: The Director', 'ESFP: The Performer', 'ESFJ: The Caregiver',
        'ENFP: The Champion', 'ENFJ: The Giver', 'ENTP: The Debater', 'ENTJ: The Commander']

BIGFIVE = ['Openness' 'Conscientiousness', 'Extraversion', 'Agreeableness', 'Neuroticism']

class Profiler:
    def __init__(self, user, pretrained: str = 'deepseek-r1:7b'):
        self.user = user 
        self.pretrained = pretrained 
        
    @property
    def memory(self) -> List[str]:
        return list(self.user.session_set.all())
        
    def analysis(self, model: str) -> str:
        history = [
            {'role': 'system', 'content': f'You are a personality profiler based on the {model} test. '},
            {'role': 'system', 'content': 
                             f'These are the latest records of {self.user.first_name}:\n' + '\n'.join(f'Day {i+1}: {mem}' for i, mem in enumerate(self.memory)) + \
                                 f"\nMake an analysis about which personality type is {self.user.first_name}. Do not write more than two paragraphs." }
        ]
        return self.get_answer(history)
    
    def stats(self, model: str) -> Dict[str, float]:
        stats = dict()
        for typ in self.types:
            value = None 
            while value is None:
                history = [
                    {'role': 'system', 'content': f'You are a personality profiler based on the {model} test. '},
                    {'role': 'system', 'content': 
                                    f'These are the latest records of {self.user.first_name}:\n' + '\n'.join(f'Day {i+1}: {mem}' for i, mem in enumerate(self.memory)) + \
                                        f'Give me the probability of {self.user.first_name} being {typ}. Only answer a number with % (e.g. 20%).'}
                ]
                answer = self.get_answer(history)
                if len(re.findall(r'\d{1,3}%', answer)) > 0:
                    value = int(re.findall(r'\d{1,3}%', answer)[0].replace('%', ''))
                    break 
            stats[typ] = value 
        return stats
                
    def get_answer(self, history: List[Dict[str, str]]) -> str:
        response = parse_response(ollama.chat(model=self.pretrained, messages=history).message.content)
        history.append({'role': 'assistant', 'content': response})
        return response
    