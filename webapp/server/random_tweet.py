import csv
import os
import random
import datetime

class RandomTweet():

    def __init__(self, path=os.path.join('data', 'tweets_sentiment.csv'), \
                num_tweets=10000):
        self.path = os.path.join(os.getcwd(), path)
        self.tweets = []
        self.num_tweets = num_tweets
        with open(self.path, 'r') as csvfile:
            reader = csv.reader(csvfile)
            count = 0
            for line in reader:
                self.tweets.append(line[5])
                count += 1
                if count >= self.num_tweets:
                    break
    
    def random_tweet(self):
        return random.choice(self.tweets)
    
    def get_random_tweets(self):
        tweets = []
        for _ in range(self.num_tweets):
            random_year = random.randint(2012, 2019)
            random_day = random.randint(1, 28)
            random_month = random.randint(1, 12)
            random_date = datetime.datetime(random_year, random_month, random_day)
            tweets.append({
                "text": self.random_tweet(), 
                "created at": random_date + random.random() * datetime.timedelta(days=1), 
                "favorites": random.randint(0, 2000),
            })
        return tweets

if __name__ == '__main__':
    rt = RandomTweet()
    print(rt.random_tweet())