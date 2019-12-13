from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from voter_data_search import VoterDataSearch
from tweet_search import TweetSearch
from tweet_auth import TweetAuth
import random

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app)

RESULTS = [
    {
    'first_name': "Hello!",
    'last_name': 'Hi there!',
    },
]
TWEETS = [[
    {
    'text': 'No Tweets',
    'created_at': 'None',
    'favorites': 0,
    }
]]

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@cross_origin(supports_credentials=True)
@app.route('/search', methods=['GET', 'POST'])
def send_search():
    response_object = {'status': 'success'}
    statuses = {
        True: 'success',
        False: 'failed'
    }
    if request.method == 'POST':
        search = VoterDataSearch()
        search_data = request.get_json()
        tw_search = TweetSearch(user=search_data.get('handle'), count=search_data.get('tweet_num'))
        first_name = search_data.get('first_name')
        last_name = search_data.get('last_name')
        middle_initial = search_data.get('middle_initial')
        success, voter_data = search.search(first_name=first_name, last_name=last_name, mi=middle_initial)
        response_object['search_result'] = voter_data
        response_object['status'] = statuses[success]
        RESULTS.append(voter_data)
        TWEETS.append(tw_search.get_ids())
    else:
        response_object['message'] = 'Nothing to get'
    return jsonify(response_object)

@cross_origin(supports_credentials=True)
@app.route('/results', methods=['GET'])
def get_results():
    res = [{'Attribute': key, 'Value': val} if val else None for key, val in RESULTS[-1].items()]
    res = [x for x in res if x]
    return jsonify(res)

@app.route('/tweets', methods=['GET'])
def get_tweets():
    return jsonify(TWEETS[-1])

@app.route('/tweet_auth', methods=['GET'])
def tweet_auth():
    tweet_texts = [t['text'] for t in TWEETS[-1]]
    ta = TweetAuth(tweet_texts)
    auth_questions = ta.gen_auth_questions()
    return jsonify([random.choice(auth_questions)])


if __name__ == '__main__':
    app.run()