from __future__ import annotations
from typing import List, Dict
import pickle

class User:
    def __init__(self, NAME: str, MEMORY: List[str], PERSONALITY: str, STATS: Dict[str, Dict[str, str]]):
        """Initializes a user of the database with relevant fields to feed the 
        prompt, such as name, daily memory and personality memory.

        Args:
            NAME (str): Name to refer to the user.
            MEMORY (str): Memory about what happened in the last conversations with the user.
            PERSONALITY (str): Summary of relevant messages that allow inferring the important
            aspects of personality. 
        """
        self.NAME = NAME 
        self.MEMORY = MEMORY 
        self.PERSONALITY = PERSONALITY
        self.STATS = STATS
        
    def save(self, path: str):
        with open(path, 'wb') as writer:
            pickle.dump(self, writer, protocol=pickle.HIGHEST_PROTOCOL)
            
    @classmethod
    def load(cls, path: str) -> User:
        with open(path, 'rb') as reader:
            user = pickle.load(reader)
        return user 