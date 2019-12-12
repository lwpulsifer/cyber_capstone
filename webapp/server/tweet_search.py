from twitter_bot import api as default_api

class TweetSearch():

    def __init__(self, user, api=default_api, count=100):
        self.api = api
        self.user = user
        self.count = count
    
    def get_tweets(self, api=None, screen_name=None, count=None):
        if not api: api = self.api
        if not screen_name: screen_name = self.user
        if not count: count = self.count
        timeline = api.GetUserTimeline(screen_name=screen_name, count=count)
        return timeline
    
    def get_ids(self, api=None, screen_name=None, count=None):
        if self.user == "": return []
        if api is None: api = self.api
        if screen_name is None: screen_name = self.user
        if count is None: count = self.count
        ids = []
        for tweet in self.get_tweets():
            ids.append({"text": tweet.text, "created at": tweet.created_at, "favorites": tweet.favorite_count})
        return ids

if __name__ == '__main__':
    tw = TweetSearch(user='adityapmathur')
    print(tw.get_ids())
    

        