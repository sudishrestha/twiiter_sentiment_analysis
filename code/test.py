from tweepy import Stream
from tweepy import OAuthHandler
from tweepy import StreamListener
#import MySQLdb
import time
import json
#        replace mysql.server with "localhost" if you are running via your own server!
#                        server       MySQL username	MySQL pass  Database name.
#conn = MySQLdb.connect("192.168.58.132","sudish","sudish","test")
#c = conn.cursor()
#consumer key, consumer secret, access token, access secret.
ckey="l7Y4fJYeVNLJ2PmThi92tJzdV"
csecret="GdEEYSip38ksU3l1mkJ3JJlSYw1SvNFLJZrlutElrKu8sTqTiZ"
atoken="3245926885-Y5GiefOTxft8Q8goxMmhTu3gSRcxwKbkqv23je3"
asecret="PCSGRIRT7D4a2OHKn1nQalI65OUOiixXjHP5IouFOk7FY"
class listener(StreamListener):
    def on_data(self, data):
        all_data = json.loads(data)
        tweet = all_data["text"]
        username = all_data["user"]["screen_name"]
        #c.execute("INSERT INTO tweet (time, username, tweet) VALUES (%s,%s,%s)",(time.time(), username, tweet))
        #conn.commit()
        with open('streams.txt', 'a') as the_file:
            the_file.write(tweet.encode('utf-8') + "\n")
        print(tweet)
        return True
    def on_error(self, status):
       print status
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["#BREXIT"])
        
        
    
