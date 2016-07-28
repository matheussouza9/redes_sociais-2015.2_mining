"""
@author: Matheus Souza
"""

from mydb import save
from tweepy import OAuthHandler, API, Cursor
import re

def qtd_requisicoes_restantes():
    return api.rate_limit_status()['resources']['search']['/search/tweets']['remaining']

hashtags = {
    '#foraCunha': 0,
    '#ficaCunha': 0,
}

consumer_key = 'kyKkew166WEpkF5Rl2jxbvrsS'
consumer_secret = 'c8f9YmGlnSoPE6ZiEBM4H7bdn5kiyzfSWbbbvTJL5c1cCKotBx'

access_token = '330276304-ljUk5LtziscapNfT4Ze9ACWt13FIkJG3QZruu16b'
access_token_secret = 'tY7SeOhJb9aeLmbRhCJQWPju8UzP27s04D6FaJKFfBZPj'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = API(auth_handler=auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

while True:
    for hashtag in hashtags:
        print(hashtag, hashtags[hashtag], 'tweets adicionados...', 'Buscando mais...')
        
        for tweet in Cursor(api.search, q=hashtag + ' -rt').items(10000):
            # remove urls do tweet
            t = re.sub(r'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))', '', tweet.text).strip()
            
            if save(t):
                print('Adicionado:', t)
                hashtags[hashtag] += 1
            else:
                print('Duplicado:', t)