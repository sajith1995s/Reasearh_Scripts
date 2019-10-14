import tweepy
import logging
import sys
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd
import warnings

consumer_key = "JjOaEAXjUq8b8PVqS1UFQpmur"
consumer_secret = "Frj1dDqF0nePQr0LYoy2cGhE8s5rmwEgFtkzYWWbJi4f5DBIMA"
access_token = "1540106498-PQZwiwzWowjjspOIErpc96hAuFKoUj8Pb2TBpLO"
access_token_secret = "b2viTdZr279qwfAp6LyH6kg4gfU0q7PCzXZpjIJGz2vVX"

# Creating the authentication object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# Setting your access token and secret
auth.set_access_token(access_token, access_token_secret)
# Creating the API object while passing in auth information
api = tweepy.API(auth)

# Language code (follows ISO 639-1 standards)
language = "en"


def twitter_rating(name):
    # The search term you want to find
    query = name
    non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
    results = []
    for tweet in tweepy.Cursor(api.search, q=query, count=100, lang="en").items():
        if "laptop" not in tweet.text:
            results.append(tweet.text.translate(non_bmp_map))
            tweet_id = tweet.id
            user = tweet.user.screen_name
            for reply in tweepy.Cursor(api.search, q='to:{}'.format(user), since_id=tweet_id, result_type='recent').items(1000):
                if hasattr(reply, 'in_reply_to_status_id_str'):
                    if reply.in_reply_to_status_id_str == tweet.id_str:
                        results.append(reply.text.translate(non_bmp_map))

    return results
