import requests
import json
import configparser
from payload import *
from utilities.resources import *
from utilities.configurations import *

# Add Book
add_book_url = get_config()["API"]["endpoint"]+ apiResources.add_book
delete_book_url = get_config()["API"]["endpoint"]+ apiResources.delete_book
headers = {"Content-Type" : "application/json"}
add_book_response = requests.post(add_book_url,
              json= add_book_payload("bh"),
              headers= headers
              )

response_json = add_book_response.json()
print(response_json)
assert add_book_response.status_code == 200
book_id = response_json["ID"]


# Delete Book
delete_book_response = requests.post(delete_book_url, json= {
                "ID" : book_id
            },
              headers= headers)

assert delete_book_response.status_code == 200

delete_book_json = delete_book_response.json()

print(delete_book_json["msg"])
assert delete_book_json["msg"] == "book is successfully deleted"
