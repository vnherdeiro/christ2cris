import praw
from time import sleep
import config
import re


def login():
    handle = praw.Reddit(username=config.username,
                        password=config.password,
                        client_id=config.client_id,
                        client_secret=config.client_secret,
                        user_agent="cristiano corrector v0.1a")
    return handle

def clean_christiano( s):
    """
    Changes christiano to cristiano while the keeping the case for each letter
    """
    return s[:1] + s[2:]

def edit_match( match):
    christ = match.group(0)
    crist = clean_christiano(christ)
    return "**" + crist + "** ~~" + christ + "~~"

def christ2crist( txt):
    """
    Updates every occurence of christiano by striking the text and prefixing the correct spelling
    """
    txt = re.sub( "christiano", edit_match, txt, flags=re.I)
    return "> " + txt.replace("\n\n", "\n\n> ") + "\n\n FTFY."

def CorrectComments( subreddit="test", last_n_comments=1000, corrected_comments=set()):
    """
    Parses the last posted comments of a subreddit
    """
    last_comments = handle.subreddit(subreddit).comments(limit=last_n_comments)
    for comment in last_comments:
        if "christiano" in comment.body.lower() and comment.id not in corrected_comments and comment.author != config.username:
            print( comment.id, comment.body)
            comment.reply( christ2crist( comment.body))
            corrected_comments.add( comment.id)


corrected_comments = set()
while True:
    try:
        handle = login()
        CorrectComments( subreddit="soccer", corrected_comments=corrected_comments)
    except:
        pass
    finally:
        sleep( 25)
