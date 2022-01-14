"""Test reading and optimizing reading operations"""

from pandas import DataFrame
from pymongo import database

from connection import client
from shared import COLLECTION_NAME, DATABASE_NAME


def find_wo_filters(collection: database.Collection) -> None:
    items = collection.find()
    items_df = DataFrame(items)  # for missing keys
    print(items_df, "\n")



def find_w_filters(collection: database.Collection) -> None:
    items = collection.find({"category": "food"})
    items_df = DataFrame(items)
    print(items_df, "\n")


def create_single_col_index(collection: database.Collection) -> None:
    collection.create_index("category")  # the most used filter


def main() -> None:
    my_connection = client()
    collection_ = my_connection[DATABASE_NAME][COLLECTION_NAME]

    find_wo_filters(collection_)
    find_w_filters(collection_)
    create_single_col_index(collection_)


if __name__ == "__main__":
    main()
