import requests
response = requests.get("http://www.omdbapi.com/?t=the frozen&apikey=35b13908")
response_jason = response.json()
# print(response_jason)
print(response_jason['Title'], response_jason['Year'], response_jason['Actors'])