__author__ = 'Michael Burdick'

import tweepy
from secrets import keys

CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SCRIPT = keys['access_token_secret']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SCRIPT)
api = tweepy.API(auth)

# I'd rather this bot not accidentally respond to some tragic, awful stuff
bad_words = ['terrorism', 'loss', 'killed', 'tragedy', 'attack', 'dead', 'death', 'tragic', 'horrifying']

pitbull = "305.jpeg"

# Start execution by gathering my most recent Tweet
my_most_recent_tweet = api.home_timeline(count = 1)

# We use this most recent Tweet as a metric, to only respond to tweets
# that have been posted since we most recently executed
most_recent_tweet_id = my_most_recent_tweet['id']

# Retrieve Tweets more recent than our most recent Tweet containing the terms "305" or "worldwide"
# I feel like "dale" has too much room for misinterpretation, and "Miami" is too broad
search_results_worldwide = api.search(q="worldwide", count = 5, since_id = most_recent_tweet_id)
search_results_305 = api.search(q="305", count = 5, since_id = most_recent_tweet_id)

for tweet in search_results_worldwide:
    innocent_tweet = not tweet['possibly_sensitive']
    tweet_content = tweet['text']
    for bad_word in bad_words:
        if tweet_content.find(bad_word):
            innocent_tweet = False
    if innocent_tweet:
        id = tweet['id']
        status = api.update_with_media(filename = "305.jpeg", status = "AIN'T NOTHIN' WORLDWIDE LIKE MR. WORLDWIDE!",
                                   in_reply_to_status_id = id)

for tweet in search_results_305:
    innocent_tweet = not tweet['possibly_sensitive']
    tweet_content = tweet['text']
    for bad_word in bad_words:
        if tweet_content.find(bad_word):
            innocent_tweet = False
    if innocent_tweet:
        id = tweet['id']
        status = api.update_with_media(filename = pitbull, status = "HEY HEY HEY, MR. 305 HERE! MIAMI!",
                                   in_reply_to_status_id = id)