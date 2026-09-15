import json

import requests
from utilities.resources import *
from utilities.configurations import *

get_book_url = get_config()["API"]["endpoint"]+ apiResources.get_book_with_author_name
response = requests.get(get_book_url,
             params={'AuthorName' : 'Rahul Shetty2'},)

# print(response.text)
# print(type(response.text))
# dict_response = json.loads(response.text)
# print(dict_response[0]["isbn"])

json_response = response.json()
print(type(json_response))
print(json_response[0]["isbn"])

assert response.status_code == 200
assert response.headers['Content-Type'] == 'application/json;charset=UTF-8'

# Retrieve the book with ISBN bbcd889
for actual_book in json_response:
    if actual_book["isbn"] == "bbcd889":
        print(actual_book)
        break
expected_book = {"book_name":"Learn Appium Automation with Java",
                 "isbn":"bbcd889",
                 "aisle":"2200227"}

assert actual_book == expected_book