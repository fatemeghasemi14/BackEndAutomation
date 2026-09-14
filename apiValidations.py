import requests

response = requests.get("http://216.10.245.166//Library/GetBook.php",
             params={'AuthorName' : 'Rahul Shetty2'},)
print(response.text)
type(response.text)