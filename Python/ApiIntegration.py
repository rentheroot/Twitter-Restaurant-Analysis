#Tweepy library imports
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Json parsing imports
import json

#Credentials to access Twitter API 
access_token = "897495635682893826-BewCW8BZtcWbn0v3FIrJSAwIisXqizw"
access_token_secret = "aggABxF67fsBSDJDkhzpBbYiUF15M0fQuPU1Xy5XqK8xT"
consumer_key = "McoZRCrbLbONTKGVHR65qLEmF"
consumer_secret = "ffNHti5vHkkzu5sehaGkpB4Pvntds8tKYZFMw1pQTXcqFCR05f"


#Override tweepy.StreamListner, print statuses to stdout
class StdOutListener(StreamListener):

    #init
    def __init__(self, api=None):
        super(StdOutListener, self).__init__()
        self.num_tweets = 0

        
    def on_data(self, data):
        with open ('TwitterOutput.txt') as f:
            self.num_tweets += 1
            if self.num_tweets < 20:
                print(data)
                return True
            else:
                return False
        

    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    #Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    restaurantName = input("Name of Restaurant")
    #Filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=[restaurantName])
