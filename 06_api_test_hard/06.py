import requests

url = input("Please enter the link: ")


response = requests.get(url)
if response.status_code < 400:
    print("200 success")
else:
    print("404 not found")