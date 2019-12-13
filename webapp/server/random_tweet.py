import csv
import os
import random

class RandomTweet():

    def __init__(self, path=os.path.join('data', 'tweets_sentiment.csv'), \
                num_tweets=10000):
        self.path = os.path.join(os.getcwd(), path)
        self.tweets = []
        with open(self.path, 'r') as csvfile:
            reader = csv.reader(csvfile)
            count = 0
            for line in reader:
                self.tweets.append(line[5])
                count += 1
                if count >= num_tweets:
                    break
    
    def random_tweet(self):
        return random.choice(self.tweets)

if __name__ == '__main__':
    rt = RandomTweet()
    print(rt.random_tweet())