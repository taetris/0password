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
    
    num_credentials = data.get('num_credentials', 1)
    length = data.get('length', 24)

    # Call your existing function
    password = push(num_credentials, length)

    # Return the generated password as JSON response
    return jsonify({'password': password}), 200

if __name__ == '__main__':
    app.run(debug=True)