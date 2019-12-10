from flask import Flask, jsonify, request
from flask_cors import CORS


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/search', methods=['GET', 'POST'])
def send_search():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        search_data = request.get_json()
        first_name = search_data.get('first_name')
        last_name = search_data.get('last_name')
        alive = search_data.get('alive')
        response_object['message'] = f'Searching for person with name {first_name} {last_name}... (Not implemented)'
    else:
        response_object['message'] = 'Nothing to get'
    return jsonify(response_object)


if __name__ == '__main__':
    app.run()