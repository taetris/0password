from pymongo import MongoClient, ASCENDING
from pymongo.errors import ConnectionFailure, OperationFailure, DuplicateKeyError
import creds
import certifi

cluster_name = "2password"
salt_db_name = "noon"
creds_db_name = "creds"

# connects to the client and returns the cluster where passwords are stored
def connect_mongoDB():
    
    try: 
        cluster = MongoClient(creds.client) 
    except ConnectionFailure:
        print("Could not connect to MongoDB")
    else:
        return cluster
# -----------------------------------------------------------------------------------------
    # Storing

# starts a session and stores creds and salt in the cluster_name named db in the cluster with failure handled
def store(generated_credentials, generated_salt):
    cluster = connect_mongoDB()
    # print("cluster:", cluster)
    session = cluster.start_session()
    db = cluster[cluster_name]

    try:
        with session.start_transaction():
            store_credentials(generated_credentials, db)
            store_salt(generated_salt, db)
            print("Both data inserted successfully")

    except OperationFailure as e:
        print("Error occurred:", e)
        session.abort_transaction()
        print("Transaction aborted. Rollback successful.")
    

# stores the credentials in the creds_db_name collection
def store_credentials(credentials, db):
    collection = db[creds_db_name]
    collection.create_index([('application', ASCENDING)], unique=True)
    collection.insert_one(credentials)

# stores the salt in the salt_db_name collection
def store_salt(salt, db):

    collection = db[salt_db_name]
    collection.insert_one(salt)
# ------------------------------------------------------
    # Fetching

# starts a fetch session and returns the username, password and salt with failure handled
def fetch(application):
    cluster = connect_mongoDB()
    session = cluster.start_session()
    db = cluster[cluster_name]
    try:
        with session.start_transaction():
            username, encrypted_password = fetch_credentials(application, db)
            salt = fetch_salt(application, db)
            print("Both data fetched successfully")
    except OperationFailure as e:
        print("Error occurred:", e)
        session.abort_transaction()
        print("Transaction aborted. Rollback successful.")
    else:
        return username, encrypted_password, salt
    
# fetches username, encrypted password from the creds_db_name db
def fetch_credentials(application, db):
    collection = db[creds_db_name]

    # Query MongoDB for documents with the specified application
    query = {"application": application}
    result = collection.find(query)
    
    for doc in result:
        # Extract relevant fields from the document
        username = doc.get("username")
        encrypted_password_binary = doc.get("encrypted_password")
        

        return username, encrypted_password_binary
    
# fetches salt from the salt_db_name db
def fetch_salt(application, db):
    collection = db[salt_db_name]

    # Query MongoDB for documents with the specified application
    query = {"application": application}
    result = collection.find(query)
    # Iterate over the results
    for doc in result:
        salt = doc.get("salt")
        return salt

# ---------------------------------------------------------------

