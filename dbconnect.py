from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, OperationFailure
import creds
def connect_mongoDB():
    
    try: 
        cluster = MongoClient(creds.client) 
    except ConnectionFailure:
        print("Could not connect to MongoDB")
        exit()
    else:
        return cluster

def store(generated_credentials, generated_salt):
    cluster = connect_mongoDB()
    print("cluster:", cluster)
    session = cluster.start_session()
    db = cluster["2password"]

    try:
        with session.start_transaction():
            store_credentials(generated_credentials, db)
            store_salt(generated_salt, db)
            print("Both data inserted successfully")

    except OperationFailure as e:
        print("Error occurred:", e)
        session.abort_transaction()
        print("Transaction aborted. Rollback successful.")

def store_salt(salt, db):
    """Store credentials in MongoDB."""
    collection = db["noon"]
    collection.insert_many(salt)

def store_credentials(credentials, db):
    """Store credentials in MongoDB."""
    collection = db["creds"]
    collection.insert_many(credentials) 

# ------------------------------------------------------
def fetch_from_mongodb(application, db):
    collection = db["creds"]

    # Query MongoDB for documents with the specified application
    query = {"application": application}
    result = collection.find(query)
    # Iterate over the results
    for doc in result:
        # Extract relevant fields from the document
        username = doc.get("username")
        encrypted_password_binary = doc.get("encrypted_password")
        

        return username, encrypted_password_binary
    
def fetch_salt(application, db):
    collection = db["noon"]

    # Query MongoDB for documents with the specified application
    query = {"application": application}
    result = collection.find(query)
    # Iterate over the results
    for doc in result:
        # Extract relevant fields from the document
        salt = doc.get("salt")
        return salt

def fetch(application):
    cluster = connect_mongoDB()
    session = cluster.start_session()
    db = cluster["2password"]
    try:
        with session.start_transaction():
            username, encrypted_password = fetch_from_mongodb(application, db)
            salt = fetch_salt(application, db)
            print("Both data fetched successfully")
    except OperationFailure as e:
        print("Error occurred:", e)
        session.abort_transaction()
        print("Transaction aborted. Rollback successful.")
    else:
        return username, encrypted_password, salt