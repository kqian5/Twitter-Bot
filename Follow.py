import tweepy
from time import sleep
from Credentials import *

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

i = input("Which users would you like to follow? Input a hashtag\n")
n = input("How many users would you like to follow?\n")

def follow(hashtag, num):
    for tweet in tweepy.Cursor(api.search, q=hashtag).items(int(num)):
        try:
            tweet.user.follow()
            sleep(5)
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break

follow(i, n)