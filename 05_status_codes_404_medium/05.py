import requests


### Test Case 1:
# url: http://35.225.243.133/bloggers/
# POST VALID DATA:
# ```
# {
#     full_name: "Idris Shabanli"
# }
# ```
# Expected status code: 201
# Expected response:
# ```
# {
#     id:	integer
#     full_name:	"Idris Shabanli"
#     created_at	($date-time)
#     updated_at ($date-time)
# }
# ```
#
# 1. Check Status code is `201`
# 2. Check `full_name` is `"Idris Shabanli"` from response

url = "http://35.225.243.133/bloggers/"
response = requests.get(url)
response_data = response.json()
print(response_data)
# print(response_data['Title'], response_data['Year'], response_data['Actors'])

