""" Tweets out an idea's descriptions. """

import users
import db
from db import config
from collections import namedtuple
from twython import Twython

twitter = Twython(
    config.get("Twitter","Consumer_Key"),
    config.get("Twitter","Consumer_Secret"),
    config.get("Twitter","Access_Token_Key"),
    config.get("Twitter","Access_Token_Secret")
)

GIST_URL = "https://gist.github.com/{0}"

Tweet = namedtuple('Tweet', 'id, msg')


def new(idea):
    """ Post a new tweet. """

    user = users.from_name(idea.username)
    if user.twitter:
        msg = ".@" + user.twitter + " - "
    else:
        msg = "New idea: "

    msg = tweetify(msg, idea.description, GIST_URL.format(idea.gistid))
    tweet = twitter.update_status(status=msg)
    # update last_tweet table
    sql = "INSERT into id_value values (?);"
    db.write(db.con, sql, tweet['id'])
    return Tweet(tweet['id'], msg)


def tweetify(msg, desc, link):
    """ Return a nice tweetable message . """

    # 22 characters are for shortening of link to 't.co'
    # Additional 1 is for ' '

    if len(msg + desc) <= 140 - 22 - 1:
        return msg + desc + ' ' + link
    else:
        return msg + link

def tweetout(status):
    twitter.update_status(status=status)
