from twython import Twython
import tweets
from db import config

twitter = TwythonStreamer(
    config["Twitter"]["Consumer_Key"],
    config["Twitter"]["Consumer_Secret"],
    config["Twitter"]["Access_Token_Key"],
    config["Twitter"]["Access_Token_Secret"]
)

temp_names = []

twitter = Twython(apikey,apisecret,oauthtoken,oauthtokensecret)

LIMIT = int(config["Constants"]["Tweets_Per_Hour"]) / 2

data = twitter.search(q='@IdeabinBot', since_id=config["Twitter"]["Last_Tweet_ID"])

for count,x in enumerate(data['statuses']):

	if count == LIMIT:
		break

   name = x['user']['screen_name']

   if name not in temp_names:
   	status="@" +name+ " Useless message ahoy!"
   	last_tweet_id= x['id']
		tweets.tweetout(status)
		temp_names.append(name)

#Save last_tweet_id in DB
