from twitter_bot import api as default_api
from twitter import TwitterError

class TweetSearch():

    def __init__(self, user, api=default_api, count=100):
        self.api = api
        self.user = user
        self.count = count
        self.error = [{"text": f"Twitter user <{self.user}> is invalid. Try again."}]
    
    def get_tweets(self, api=None, screen_name=None, count=None):
        if not api: api = self.api
        if not screen_name: screen_name = self.user
        if not count: count = self.count
        try:
            timeline = api.GetUserTimeline(screen_name=screen_name, count=count)
        except TwitterError as e:
            return None
        return timeline
    
    def get_ids(self, api=None, screen_name=None, count=None):
        if self.user == "": return []
        if api is None: api = self.api
        if screen_name is None: screen_name = self.user
        if count is None: count = self.count
        ids = []
        if self.get_tweets():
            for tweet in self.get_tweets():
                ids.append({"text": tweet.text, "created at": tweet.created_at, "favorites": tweet.favorite_count})
            success = True
        else:
            ids = self.error
            success = False
        return success, ids

if __name__ == '__main__':
    tw = TweetSearch(user='adityapmathur')
    print(tw.get_ids())
    

        