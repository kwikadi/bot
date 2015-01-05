from twython import TwythonStreamer
import tweets
from db import config

twitter = TwythonStreamer(
    config["Twitter"]["Consumer_Key"],
    config["Twitter"]["Consumer_Secret"],
    config["Twitter"]["Access_Token_Key"],
    config["Twitter"]["Access_Token_Secret"]
)

class botStreamer(TwythonStreamer):
	def on_success(self, data):
		name = data['user']['screen_name']
		status= "@" + name + " Useless message because my creator is a lazy bum."
		tweets.tweetout(status)

stream = botStreamer(apikey,apisecret,oauthtoken,oauthtokensecret)

stream.statuses.filter(track='@IdeabinBot')
