import tweepy
from time import sleep
from credentials import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

<<<<<<< HEAD
my_file=open('../data/processed/working-V2-sentences.txt','r', encoding='utf-8')
=======
my_file=open('../data/processed/working-sentences.txt','r', encoding='utf-8')
>>>>>>> db8b3b02a6827c240162b97136e2826a70c5e233
file_lines=my_file.readlines()
my_file.close()

# Tweet a line every 60 minutes
def tweet():
    for line in file_lines:
        try:
             print(line)
             if line != '\n':
                 api.update_status(line)
                 sleep(3600)
             else:
                pass
        except tweepy.TweepError as e:
            print(e.reason)
            sleep(2)

tweet()
