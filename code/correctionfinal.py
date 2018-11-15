from tweepy import Stream
from tweepy import OAuthHandler
from tweepy import StreamListener
#import MySQLdb
import multiprocessing
import time
import json
import sys

#        replace mysql.server with "localhost" if you are running via your own server!
#                        server       MySQL username	MySQL pass  Database name.
#conn = MySQLdb.connect("192.168.58.132","sudish","sudish","test")
#c = conn.cursor()
#consumer key, consumer secret, access token, access secret.
ckey="l7Y4fJYeVNLJ2PmThi92tJzdV"
csecret="GdEEYSip38ksU3l1mkJ3JJlSYw1SvNFLJZrlutElrKu8sTqTiZ"
atoken="3245926885-Y5GiefOTxft8Q8goxMmhTu3gSRcxwKbkqv23je3"
asecret="PCSGRIRT7D4a2OHKn1nQalI65OUOiixXjHP5IouFOk7FY"
def some_task():
    class listener(StreamListener):
        def on_data(self, data):
            all_data = json.loads(data)
            tweet = all_data["text"].encode('utf-8')
            username = all_data["user"]["screen_name"]
            with open('streams.dat', 'a') as the_file:
                the_file.write(tweet.encode('utf-8') + "\n")
            print(tweet)
            return True
        def on_error(self, status):
           print status
    auth = OAuthHandler(ckey, csecret)
    auth.set_access_token(atoken, asecret)
    twitterStream = Stream(auth, listener())
    twitterStream.filter(track=[str(sys.argv[2])])

if __name__ == '__main__':
    # Start foo as a process
    p = multiprocessing.Process(target=some_task)
    p.start()
    k = int(sys.argv[1])
    # Wait 10 seconds for foo
    time.sleep(k)

    # Terminate foo
    p.terminate()

    # Cleanup
    p.join()
    

