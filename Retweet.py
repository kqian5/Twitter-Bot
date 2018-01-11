import tweepy
from time import sleep
from Credentials import *

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

i = input("What tweets would you like to retweet? Input a hashtag\n")
n = input("How many retweets would you like?\n")

def retweet(hashtag, num):
    for tweet in tweepy.Cursor(api.search, q=hashtag).items(int(num)):
        try:
            tweet.retweet()
            sleep(5)
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break

retweet(i, n)

