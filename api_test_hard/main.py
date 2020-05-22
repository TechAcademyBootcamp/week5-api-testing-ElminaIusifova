import requests

def magic(name):
    url = "http://35.225.243.133/bloggers/"
    response = requests.get(url)
    response_data = response.json()
    status = response.status_code
    print(status)
    print(response_data)
    x = requests.post(url, name)
    print(x.json())
    # y = requests.post(url, id)
    # print(y.json())






