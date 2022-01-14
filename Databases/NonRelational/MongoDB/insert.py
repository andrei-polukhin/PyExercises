"""Test insert operations via MongoDB client"""
from datetime import datetime

import pytz
from pymongo import database, MongoClient

from connection import client
from shared import COLLECTION_NAME, DATABASE_NAME


def create_database(client: MongoClient) -> database.Database:
    return client[DATABASE_NAME]


def create_collection(database_: database.Database) -> database.Collection:
    return database_[COLLECTION_NAME]


def insert_into_collection(collection: database.Collection) -> None:
    # insert many
    item_1 = {
        "_id" : "U1IT00001",
        "item_name" : "Blender",
        "max_discount" : "10%",
        "batch_number" : "RR450020FRG",
        "price" : 340,
        "category" : "kitchen appliance"
    }
    item_2 = {
        "_id" : "U1IT00002",
        "item_name" : "Egg",
        "category" : "food",
        "quantity" : 12,
        "price" : 36,
        "item_description" : "brown country eggs"
    }
    collection.insert_many([item_1,item_2])

    # insert one
    item_3 = {
        "item_name" : "Bread",
        "quantity" : 2,
        "ingredients" : "all-purpose flour",
        "expiry_date" : pytz.utc.localize(datetime(2022, 2, 14, 16, 0, 0))
    }
    collection.insert_one(item_3)


def main() -> None:
    my_connection = client()

    my_database = create_database(my_connection)
    my_collection  = create_collection(my_database)
    insert_into_collection(my_collection)


if __name__ == "__main__":
    main()
