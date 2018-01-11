import tweepy, time, sys

argfile = str(sys.argv[1])

CONSUMER_KEY = '79qJzHuheVEH2Kd8J2zQyoXnQ'
CONSUMER_SECRET = 'jIBFRvY4xFy1Y8WqglUgDIdNgna9bOtw9VgpEWc3DrZfAHPgka'
ACCESS_KEY = '1666297878-htXQH7aKedXCV3me14K7hFwDlk2bm9d6UueegHM'
ACCESS_SECRET = 'Mb2p7PMy6LG905WwgR6Hu5mLgtK9tTWsvrWuiJXP1xzMS'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


filename = open(argfile, 'r')
f = filename.readlines()
filename.close()

for line in f:
    api.update_status(line)
    time.sleep(1000)