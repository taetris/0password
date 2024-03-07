from flask import Flask, jsonify, request
from .main import push, pull
from flask_cors import CORS 

app = Flask(__name__)
CORS(app)  
# Define a Flask route for your API endpoint
@app.route('/suggestor', methods=['POST'])
def generate_credentials():
    # Get parameters from the request (assuming JSON payload)
    data = request.json
    application = data.get('application')
    username = data.get('username')
    length = data.get('length', 24)

    # Call the push function with provided parameters
    password = push(application, username, length)

     # Return a response containing JavaScript to copy the password to the clipboard
    response = f"""
        <script>
            var tempInput = document.createElement("textarea");
            tempInput.value = "{password}";
            document.body.appendChild(tempInput);
            tempInput.select();
            document.execCommand("copy");
            document.body.removeChild(tempInput);
            alert("Password copied to clipboard: {password}");
        </script>
    """
    return response
    # Return the generated password as JSON response
    # return jsonify({'password': password}), 200

if __name__ == '__main__':
    app.run(debug=True)