from pymongo import MongoClient


def store_in_mongodb(credentials):
    """Store credentials in MongoDB."""
    
    cluster = MongoClient("mongodb+srv://076bei047tripti:u3z1Sfx0JieW6yNG@clusteruno.ds5kfqa.mongodb.net/")
    db = cluster["2password"]
    collection = db["trial-1"]
    collection.insert_many(credentials)