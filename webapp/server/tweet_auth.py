import random
from random_tweet import RandomTweet

class TweetAuth():

    def __init__(self, tweets):
        self.tweets = tweets
    
    def gen_auth_questions(self):
        questions = []
        rt = RandomTweet()
        for tweet in self.tweets:
            possibles = [[rt.random_tweet() for _ in range(3)] + [tweet]]
            random.shuffle(possibles)
            new_question = {
                'question': "Which one of these is one of your tweets?",
                'tag': 'tweet',
                'possibles': possibles,
                'correct': tweet,
            }
            questions.append(new_question)
        return questions

if __name__ == '__main__':
    auth = TweetAuth(["If I weren't so beautiful, I'd probably be a bouncer"])
    print(auth.gen_auth_questions())
        