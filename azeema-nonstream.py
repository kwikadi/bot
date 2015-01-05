from twython import Twython
import tweets
from db import *

twitter = TwythonStreamer(
    config["Twitter"]["Consumer_Key"],
    config["Twitter"]["Consumer_Secret"],
    config["Twitter"]["Access_Token_Key"],
    config["Twitter"]["Access_Token_Secret"]
)

sql = "SELECT last_tweet_id FROM values"
last_tweet_id = db.read(db.con, sql, None)
temp_names = []

twitter = Twython(apikey,apisecret,oauthtoken,oauthtokensecret)

LIMIT = int(config["Constants"]["Tweets_Per_Hour"]) / 2

data = twitter.search(q='@IdeabinBot', since_id=last_tweet_id)

for count,x in enumerate(data['statuses']):

	if count == LIMIT:
		break

   name = x['user']['screen_name']

   if name not in temp_names:
   	status="@" +name+ " Useless message ahoy!"
   	last_tweet_id= x['id']
		tweets.tweetout(status)
		temp_names.append(name)

sql = "UPDATE values SET last_tweet_id = " + str(last_tweet_id)
db.write(db.con, sql)
