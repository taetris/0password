A simple cmd line password manager I made for myself that generates passwords,  and uses Argon2 for encryption and stores your passwords at your provided database and fetches and copies it to your clipboard when you retrieve it by the website name.

Download all dependencies from requirements.txt and run main.py in src folder

Important Notes:
1. the creds.py currently contains the following information:
    client = "mongodb+srv://xxxx@clusteruno.xxxx.mongodb.net/"
    master_password = "xxxx"
    default_username = "xxxx"

Basic Troubleshooting:
1. SSL handshake errors:
- Always whitelist your IP on mongodb before you try to access.
