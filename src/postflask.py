import requests

# URL of your Flask app
url = 'http://localhost:5000/suggestor'  # Update the URL if necessary

# JSON data to send in the request
data = {
    'num_credentials': 1,
    'length': 24
}

# Send POST request with JSON data
response = requests.post(url, json=data)

# Print the response
print(response.json())
