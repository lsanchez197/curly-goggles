# Learning to Scrape Data
#
# Lacey Sanchez

import tweepy
import json

# Specify the account credentials in the following variables:
consumer_key = 'dkk4wvPa3U6M8j1Mtx6csmmXz'
consumer_secret = '3vOBDYieIuYNi1Q1seLynsZTPDwZCYWaHRi3o5THqEP12cDyUm'
access_token = '1866054085-tuJ555pjU7fKyoHUeQbChBFtHBUsBDJRO7gzPHp'
access_token_secret = 'T1Dw8oLR4bkMfLojUI1zuBIPiChvMxIsK3GUHWLnmo2Jx'


# This listener will print out all Tweets it receives
class PrintListener(tweepy.StreamListener):
    def on_data(self, data):
        # Decode the JSON data
        tweet = json.loads(data)

        # Print out the Tweet
        print('@%s: %s' % (tweet['user']['screen_name'], tweet['text'].encode('ascii', 'ignore')))

    def on_error(self, status):
        print(status)


if __name__ == '__main__':
    listener = PrintListener()

    # Show system message
    print('I will now print Tweets containing "Python"! ==>')

    # Authenticate
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # Connect the stream to our listener
    stream = tweepy.Stream(auth, listener)
    stream.filter(track=['Python'])