#!/usr/bin/env python3
"""Task 12.
"""
from pymongo import MongoClient


def print_nginx_logs(nginx_collection):
    """Prints stats about Nginx logs."""

    print(f"{nginx_collection.count_documents({})} logs")
    print("Methods:")

    methods_list = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    for method in methods_list:
        req_count = len(list(nginx_collection.find({"method": method})))
        print("\tmethod {}: {}".format(method, req_count))

    status_checks_count = len(
        list(nginx_collection.find({"method": "GET", "path": "/status"}))
    )

    print(f"{status_checks_count} status check")


def run():
    """Nginx stats logs stored in MongoDB."""

    client = MongoClient("mongodb://127.0.0.1:27017")
    print_nginx_logs(client.logs.nginx)


if __name__ == "__main__":
    run()
