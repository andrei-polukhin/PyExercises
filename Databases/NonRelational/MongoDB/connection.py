"""Get a client-side representation of a MongoDB cluster"""
import os
import sys
from functools import lru_cache

from pymongo import MongoClient

#: Cluster config
try:
    USERNAME = os.environ['MONGO_USERNAME']
    PASSWORD = os.environ['MONGO_PASSWORD']
    CLUSTER = os.environ['MONGO_CLUSTER']
except KeyError:
    print("Credentials are NOT configured!")
    sys.exit(0)

CONNECTION_STRING = (
    f"mongodb+srv://{USERNAME}:{PASSWORD}@{CLUSTER}.mongodb.net"
     "/myFirstDatabase"
)


class MongoClientResource:
    @lru_cache(maxsize=None)
    def __call__(self) -> MongoClient:
        if self is not client:
            return client()

        return self._create_connection()

    @staticmethod
    def _create_connection() -> MongoClient:
        return MongoClient(CONNECTION_STRING)


client = MongoClientResource()
