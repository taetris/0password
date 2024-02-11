from pymongo import MongoClient


def store_in_mongodb(credentials):
    """Store credentials in MongoDB."""
    
    cluster = ""
    db = cluster["2password"]
    collection = db["trial-1"]
    collection.insert_many(credentials)