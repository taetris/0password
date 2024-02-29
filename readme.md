A simple cmd line password manager I made for myself that generates passwords,  and uses Argon2 for encryption and stores your passwords at your provided database and fetches and copies it to your clipboard when you retrieve it by the website name.

Download all dependencies from requirements.txt in a virtual environment and run the main.py file in the src folder.

To retrieve a password from db, go:
    python main.py pull

To generate and store a password, go:
    python main.py push

Important Notes:

1. the creds.py currently contains the following information:
    client = "mongodb+srv://xxxx@clusteruno.xxxx.mongodb.net/"
    default_master_password = "xxxx"
    default_username = "xxxx"

Basic Troubleshooting:

1. SSL handshake errors:
- Always whitelist your IP on mongodb before you try to access.

2. Always make a virtual environment and source it before you try to run the program.
