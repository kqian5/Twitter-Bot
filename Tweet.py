import tweepy, time, sys
from Credentials import *


# import own credentials
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

def tweet():
    file = input("Include the text file you would like to tweet.")
    filename = open(file, 'r')
    f = filename.readlines()
    filename.close()
    for line in f:
        api.update_status(line)
        time.sleep(20)

tweet()

