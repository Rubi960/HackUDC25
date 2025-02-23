from typing import Dict, List 
from chat.assistant import parse_response, Assistant
import ollama, re 
from chat.models import User


ENNEAGRAM = ['Type 1: The Perfectionist', 'Type 2: The Giver', 'Type 3: The Achiever',
             'Type 4: The Individualist', 'Type 5: The Investigator', 'Type 6: The Skeptic',
             'Type 7: The Enthusiast', 'Type 8: The Challenger', 'Type 9: The Peacemaker']
MBTI = ['ISTJ: The Inspector', 'ISTP: The Crafter', 'ISFJ: The Protector', 'ISFP: The Artist',
        'INFJ: The Advocate', 'INFP: The Mediator', 'INTJ: The Architect', 'INTP: The Thinker',
        'ESTP: The Persuader', 'ESTJ: The Director', 'ESFP: The Performer', 'ESFJ: The Caregiver',
        'ENFP: The Champion', 'ENFJ: The Giver', 'ENTP: The Debater', 'ENTJ: The Commander']

BIGFIVE = ['Openness' 'Conscientiousness', 'Extraversion', 'Agreeableness', 'Neuroticism']

class Profiler:
    """
    Class for personality profiling. Contains methods for analyzing the user's personality.
    Input: User - The user object representing the current user.
    Output: None
    """
    def __init__(self, user: User, pretrained: str = 'deepseek-r1:32b'):
        """Initializes the profiler.

        Args:
            user (User): Input user.
            pretrained (str): Profiler model to analyze the user's  personality. Defaults to 'deepseek-r1:32b'.
        """
        self.user = user 
        self.pretrained = pretrained 
        
    @property
    def user_memory(self) -> List[str]:
        """Gets the list of previous summaries for the input user."""
        return list(map(str, self.user.session_set.all()))
        
    def analysis(self, model: str) -> str:
        """Performs a personality analysis given an specific model.

        Args:
            model (str): Personality model (e.g. MBTI).

        Returns:
            str: Personality analysis.
        """
        print(self.user_memory)
        history = [
            {'role': 'system', 'content': f'You are a personality profiler based on the {model} test. '},
            {'role': 'system', 'content': 
                             f'These are the latest things that happened to {self.user.first_name}:\n' + '\n'.join(f'Day {i+1}: {mem}' for i, mem in enumerate(self.user_memory)) + \
                                 f"\nMake an analysis about the {model} personality type. Do not write more than two paragraphs." }
        ]
        return self.get_answer(history)
    
    def stats(self, model: str) -> Dict[str, float]:
        """
        Gets the statistics to associate the input user to the different personality types of a given model
        
        Args:
            model (str): Personality model (e.g. MBTI).

        Returns:
            Dict[str, float]: User's probability to belong to an specific personality type.
        """
        if model.lower() == 'enneagram':
            types = ENNEAGRAM
        elif model.lower() == 'mbti':
            types = MBTI
        else:
            types = BIGFIVE
        stats = dict()
        for typ in types:
            value = None 
            while value is None:
                history = [
                    {'role': 'system', 'content': f'You are a personality profiler based on the {model} test. '},
                    {'role': 'system', 'content': 
                                    f'These are the latest things that happened to {self.user.first_name}:\n' + '\n'.join(f'Day {i+1}: {mem}' for i, mem in enumerate(self.user_memory)) + \
                                        f'Give me the probability of {self.user.first_name} being {typ}. Only answer a number with % (e.g. 20%).'}
                ]
                answer = self.get_answer(history)
                if len(re.findall(r'\d{1,3}%', answer)) > 0:
                    value = int(re.findall(r'\d{1,3}%', answer)[0].replace('%', ''))
                    break 
            stats[typ] = value 
        return stats
                
    def get_answer(self, history: List[Dict[str, str]]) -> str:
        """Gets the answer of the LLM from an input history."""
        response = parse_response(ollama.chat(model=self.pretrained, messages=history).message.content)
        history.append({'role': 'assistant', 'content': response})
        return response
    