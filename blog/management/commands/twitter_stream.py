__author__ = 'rakesh'

from blog.models import Twitter
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener, Stream
import time
import json
import sqlite3 as lite
import sys

ckey = '3FfsKyHKlDWOmpwP57ECPIioY'
csecret = 'dV3ZomRgR255MVlOptOTrJqa6zl9oEpbZDR0c0Cggn9qQM665g'
atoken = '39455623-3OplCdYC436UyjjQU6nCBiDL2IlaPwY0ATqtjrpEm'
asecret = 'HtXvx6zuZzDAODVXVYTfnzoNpDAJwQoLueFhMNZIPHWlw'

#cur.execute("CREATE TABLE tweet(time varchar(255), tweet varchar(255), latitude varchar(255), longitude varchar(255))")

class listener(StreamListener):

    def on_data(self, data):
        all_data = json.loads(data)  #twitter data is coming from here
        try:
            coordinate = all_data['coordinates']
        except:
            print all_data
        try:

            if coordinate:
                coordinate_list = coordinate.items()
                latitude = coordinate_list[1][1][0]
                longitude = coordinate_list[1][1][1]
                tweet = all_data['text']
                print tweet, latitude, longitude
                text = str((latitude, longitude))
                Twitter.objects.create(timestamp=time.time(), tweets= tweet, latitude = latitude,
                                                                                longitude = longitude)
        except:
            pass

        return True

    def on_error(self, status):
        print status

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["Python", "Java", "Scala", "Ruby", "Haskell"])  #filter is here
#twitter filter is coming here and you can filter as per your requirement location is here
#location filter will come from here





