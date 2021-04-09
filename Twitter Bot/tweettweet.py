import tweepy
import time

auth = tweepy.OAuthHandler('consumer_key', 'consumer_secret')
auth.set_access_token('access_token', 'access_token_secret')

api = tweepy.API(auth)
user = api.me()

# Pause the api access if reached the limit
def limit_handle(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError():
        time.sleep(300)

def follow_back():
    # Follow back some of the followers that have more than 100 followers
    for follower in tweepy.Cursor(api.followers).items():
        if follower.followers_count> 100:
            #print(follower.name)
            follower.follow()
            break


def like_retweet_tweets_with_python(search_string = 'python', number_of_tweets = 2):
    # like and retweet number_of_tweets with search_string in them
    for tweet in tweepy.Cursor(api.search, search_string).items(number_of_tweets):
        try:
            tweet.favorite()
            tweet.retweet()
            print('I like that tweet!')

        except tweepy.TweepError as err:
            print(err.reason)
        except StopIteration:
            break
        
if __name__ == '__main__':
    follow_back()
    like_retweet_tweets_with_python('AI', 5)

    


