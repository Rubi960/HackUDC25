import pandas as pd 
import re, ollama
from chat import Chat 
from user import User
from profiler import Profiler, MBTI, ENNEAGRAM

# data extracted from database
NAME = 'Rob'

# data extracted from the personality database
MODEL = 'MBTI'
MODEL_DATA = pd.read_excel(f'{MODEL}.xlsx', header=0, index_col=0)


if __name__ == '__main__':
    # first day 
    # chat = Chat(conver='deepseek-r1:32b', memory='deepseek-r1:32b')
    # user = User('Tiana', MEMORY=[], PERSONALITY=None, STATS=dict())
    # user = chat.first(user)
    # user.save(f'{user.NAME}-day1.pickle')
    
    # user = User.load(f'{user.NAME}-day1.pickle')
    # chat = Chat(conver='deepseek-r1:32b', memory='deepseek-r1:32b')
    # user = chat.start(user)
    # user.save(f'{user.NAME}-day2.pickle')
    
    user = User.load(f'Tiana-day2.pickle')
    profiler = Profiler(pretrained='deepseek-r1:32b', model='Enneagram', types=ENNEAGRAM)
    print(profiler.user_view(user).PERSONALITY)
    
    