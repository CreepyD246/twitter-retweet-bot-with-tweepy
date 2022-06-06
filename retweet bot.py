# Importing Tweepy and time
import tweepy
import time

# Credentials
api_key = "INSERT API KEY"
api_secret = "INSERT SECRET API KEY"
bearer_token = r"INSERT BEARER TOKEN"
access_token = "INSERT ACCESS TOKEN"
access_token_secret = "INSERT SECRET ACCESS TOKEN"

# Gainaing access and connecting to Twitter API using Credentials
client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)

auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)


# Bot searches for tweets containing certain keywords
class MyStream(tweepy.StreamingClient):

    # This function gets called when a tweet passes the stream
    def on_tweet(self, tweet):

        # Retweeting the tweet
        try:
            # Retweet
            client.retweet(tweet.id)

            # Printing Tweet
            print(tweet.text)

            # Delay
            #time.sleep(1)

        except Exception as error:
            # Error
            print(error)


# Creating Stream object
stream = MyStream(bearer_token=bearer_token)

# Adding terms to search rules
rule = tweepy.StreamRule("(#Python OR #programming) (-is:retweet -is:reply)") 
stream.add_rules(rule, dry_run=True)

# Starting stream
stream.filter()
