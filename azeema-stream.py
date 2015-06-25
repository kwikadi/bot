from twython import TwythonStreamer
import tweets
import db

class botStreamer(TwythonStreamer):
	def on_success(self, data):
		name = data['user']['screen_name']
		status= "@" + name + " I need to think up of something!"
		tweet = tweets.tweetout(status)
		if tweet:
			sql = "INSERT into retweets values (?), now() ;"
			db.write(db.con, sql, tweet['id'])

stream = botStreamer(
    db.config.get("Twitter","Consumer_Key"),
    db.config.get("Twitter","Consumer_Secret"),
    db.config.get("Twitter","Access_Token_Key"),
    db.config.get("Twitter","Access_Token_Secret")
)

stream.statuses.filter(track='@IdeabinBot')
