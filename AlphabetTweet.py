import tweepy, time, sys
from Credentials import *


argfile = str(sys.argv[1])

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

def tweet():
    filename = open(argfile, 'r')
    f = filename.readlines()
    filename.close()
    for line in f:
        api.update_status(line)
        time.sleep(20)

tweet()

