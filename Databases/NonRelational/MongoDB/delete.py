"""Clear all the created data"""
from pymongo import MongoClient

from connection import client
from shared import COLLECTION_NAME, DATABASE_NAME


def drop_collection(connection_: MongoClient) -> None:
    collection_ = connection_[DATABASE_NAME][COLLECTION_NAME]
    collection_.drop()


def drop_database(connection_: MongoClient) -> None:
    connection_.drop_database(DATABASE_NAME)


def main() -> None:
    my_connection = client()

    drop_collection(my_connection)
    drop_database(my_connection)


if __name__ == "__main__":
    main()
