from twython import Twython
import tweets
import db
from collections import namedtuple
import ideas

twitter = Twython(
    db.config.get("Twitter","Consumer_Key"),
    db.config.get("Twitter","Consumer_Secret"),
    db.config.get("Twitter","Access_Token_Key"),
    db.config.get("Twitter","Access_Token_Secret")
)

sql = "SELECT last_tweet_id FROM values"
last_tweet_id = db.read(db.con, sql)
temp_names = []

Tweet = namedtuple('Tweet', 'id, msg')

LIMIT = int(db.config.get("Constants","Tweets_Per_Hour")) / 2

data = twitter.search(q='@IdeabinBot', since_id=last_tweet_id)

for count,x in enumerate(data['statuses']):

  if count == LIMIT:
    break
  else:
    name = x['user']['screen_name']

    if name not in temp_names:
      status="@" +name+ " Useless message ahoy!"
      last_tweet_id= x['id']
      tweet = tweets.tweetout(status)
      temp_names.append(name)
      sql = "INSERT into retweets values (?), now() ;"
      db.write(db.con, sql, tweet['id'])


sql = "UPDATE values SET last_tweet_id = (?)"
db.write(db.con, sql, last_tweet_id)
