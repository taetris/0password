import requests

# URL of your Flask app
url = 'http://localhost:5000/suggestor'  # Update the URL if necessary

# JSON data to send in the request
data = {
    'application': 'flipkart',  # Replace 'your_application_name' with the actual application name
    'username': 'user8',  # Replace 'your_username' with the actual username
    'length': 24
}

# Send POST request with JSON data
response = requests.post(url, json=data)

# Print the response
print(response.json())
