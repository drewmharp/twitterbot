import time
import sys
import tweepy
import random
# from credentials import *  # use this one for testing

# use this for production; set vars in heroku dashboard
from os import environ
from envVar import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET

#CONSUMER_KEY = environ['CONSUMER_KEY']
#CONSUMER_SECRET = environ['CONSUMER_SECRET']
#ACCESS_KEY = environ['ACCESS_KEY']
#ACCESS_SECRET = environ['ACCESS_SECRET']

INTERVAL = 60 * 60 * 3.5  # tweet every 6 hours
# INTERVAL = 15  # every 15 seconds, for testing

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

templates = ["How would you define success?", "What is your personal definition of success?", "When does one reach true success?", "What is success to you?"]
count = 0
while True:
    print("Begin")
    if(count >= len(templates)):
        count = 0
    results = api.search(q = "\"success is\"" , lang = "en", count = 10, result_type = "recent")
    #api.update_status(tweet)
    user_tweet = results[random.randint(0,9)]
    username = user_tweet.user.screen_name
    tweet = ("@%s " + templates[count] + "\n" + "https://twitter.com/%s/status/%s") % (username,username,user_tweet.id)
    api.update_status(status = tweet,in_reply_to_status_id = user_tweet.id, auto_populate_reply_metadata = True)
    count+=1
    time.sleep(INTERVAL)
