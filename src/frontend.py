from flask import Flask, jsonify, request
from .main import push, pull

app = Flask(__name__)

# Define a Flask route for your API endpoint
@app.route('/suggestor', methods=['POST'])
def generate_credentials():
    # Get parameters from the request (assuming JSON payload)
    data = request.json
    application = data.get('application')
    username = data.get('username')
    length = data.get('length', 24)

    # Call the push function with provided parameters
    # password = push(application, username, length)

    # Return the generated password as JSON response
    return jsonify({'password': 'passwordyy'}), 200

if __name__ == '__main__':
    app.run(debug=True)