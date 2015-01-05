from twython import Twython
import tweets
from db import config

twitter = TwythonStreamer(
    config["Twitter"]["Consumer_Key"],
    config["Twitter"]["Consumer_Secret"],
    config["Twitter"]["Access_Token_Key"],
    config["Twitter"]["Access_Token_Secret"]
)

twitter = Twython(apikey,apisecret,oauthtoken,oauthtokensecret)

names=[]

data = twitter.search(q='@IdeabinBot', since_id=config["Twitter"]["Last_Tweet_ID"])

for x in data['statuses']:
   names.append(x['user']['screen_name'])

for name in names:
	status="@" +name+ " Useless message ahoy!"
	tweets.tweetout(status)
