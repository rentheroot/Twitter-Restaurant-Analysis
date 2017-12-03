#Tweepy library imports
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import subprocess

#Json parsing imports
import json

#Credentials to access Twitter API 
access_token = "897495635682893826-BewCW8BZtcWbn0v3FIrJSAwIisXqizw"
access_token_secret = "aggABxF67fsBSDJDkhzpBbYiUF15M0fQuPU1Xy5XqK8xT"
consumer_key = "McoZRCrbLbONTKGVHR65qLEmF"
consumer_secret = "ffNHti5vHkkzu5sehaGkpB4Pvntds8tKYZFMw1pQTXcqFCR05f"

restaurantName = input("Name of Restaurant or buisiness")


with open ('TwitterOutput.txt', 'w') as f:
    f.close()
with open ('TwitterFormatted.txt', 'w') as f:
    f.close()
#Override tweepy.StreamListner, print statuses to stdout
class StdOutListener(StreamListener):

    #init
    def __init__(self, api=None):
        super(StdOutListener, self).__init__()
        self.num_tweets = 0

        
    def on_data(self, data):
            all_data = json.loads(data)
            tweet = all_data["text"]
            tweet = tweet.replace('\n', '')

            
            with open  ('TwitterFormatted.txt', 'a') as f1:
                try:
                    f1.write(str(tweet))
                    f1.write(';')
                    
                except IOError:
                    pass
                    f1.close

                self.num_tweets += 1
                if self.num_tweets < 5:
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

    stream.filter(track=[restaurantName])


subprocess.call(['java', '-jar', 'readinput.jar'])
    
