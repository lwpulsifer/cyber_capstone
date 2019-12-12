#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Downloads all tweets from a given user.
Uses twitter.Api.GetUserTimeline to retreive the last 3,200 tweets from a user.
Twitter doesn't allow retreiving more tweets than this through the API, so we get
as many as possible.
t.py should contain the imported variables.
"""

import json
import sys

import twitter
from twitter_bot import api

def get_tweets(api=None, screen_name=None, count=200):
    timeline = api.GetUserTimeline(screen_name=screen_name, count=count)
    earliest_tweet = min(timeline, key=lambda x: x.id).id
    print("getting tweets before:", earliest_tweet)

    while True:
        tweets = api.GetUserTimeline(
            screen_name=screen_name, max_id=earliest_tweet, count=200
        )
        new_earliest = min(tweets, key=lambda x: x.id).id

        if not tweets or new_earliest == earliest_tweet:
            break
        else:
            earliest_tweet = new_earliest
            print("getting tweets before:", earliest_tweet)
            timeline += tweets

    return timeline[:count]


if __name__ == "__main__":
    screen_name = sys.argv[1]
    count = int(sys.argv[2])
    print(screen_name)
    timeline = get_tweets(api=api, screen_name=screen_name, count=count)
    print(dir(timeline[0]))
    for tweet in timeline:
        print(tweet.text)

    with open('examples/timeline.json', 'w+') as f:
        f.truncate(0)
        for tweet in timeline:
            f.write(json.dumps(tweet._json))
            f.write('\n')