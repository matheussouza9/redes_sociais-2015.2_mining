"""
@author: Matheus Souza
"""

from pony.orm import Database, PrimaryKey, Optional, db_session, commit ,CommitException

db = Database(
    'mysql',
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'redes_sociais_tt'
)

class Tweet(db.Entity):
    id = PrimaryKey(int, auto = True)
    #text = Required(str)
    text = Optional(str)
    hashtag = Optional(int)
    
db.generate_mapping()

@db_session
def getAllTweets():
    return Tweet.select()

@db_session
def save(t):
    try:
        _ = Tweet(text=t)
        commit()
        return True
    except CommitException:
        return False