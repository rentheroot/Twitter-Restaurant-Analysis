#Tweepy library imports
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from geopy.geocoders import Nominatim 


#Json parsing imports
import json

#Credentials to access Twitter API 
access_token = "897495635682893826-BewCW8BZtcWbn0v3FIrJSAwIisXqizw"
access_token_secret = "aggABxF67fsBSDJDkhzpBbYiUF15M0fQuPU1Xy5XqK8xT"
consumer_key = "McoZRCrbLbONTKGVHR65qLEmF"
consumer_secret = "ffNHti5vHkkzu5sehaGkpB4Pvntds8tKYZFMw1pQTXcqFCR05f"

restaurantName = input("Name of Restaurant")
restaurantLocation = input("Location of restaurant (city, state, country)")
geolocator = Nominatim()
location = geolocator.geocode(restaurantLocation)
location= location.raw
boundingValues = location['boundingbox']

with open ('TwitterOutput.txt', 'w') as f:
    f.close()
#Override tweepy.StreamListner, print statuses to stdout
class StdOutListener(StreamListener):

    #init
    def __init__(self, api=None):
        super(StdOutListener, self).__init__()
        self.num_tweets = 0

        
    def on_data(self, data):
        
        if restaurantName in status.text.lower():
            all_data = json.loads(data)
            
            tweet = all_data["text"]
            tweet2 = tweet.replace(",", '')
            
            with open  ('TwitterFormatted.txt', 'a') as f1:
                try:
                    f1.write(str(tweet2))
                    f1.write(',')
                    f1.close
                except IOError:
                    pass
                    f1.close

            with open ('TwitterOutput.txt', 'a') as f:
                self.num_tweets += 1
                if self.num_tweets < 5:
                    f.write(data)
                    return True
                else:
                    return False
                    f.close()

    def on_error(self, status):
        print(status)
        


if __name__ == '__main__':

    #Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #print(location.address)
    #print((location.latitude, location.longitude))
    
    
    #Filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(locations=[boundingValues])
    
