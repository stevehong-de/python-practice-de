# Disney character data via rest api from https://disneyapi.dev/docs/
# There is no authentication required for this api

import requests

# Root URL for the Disney API
ROOT_URL = "https://api.disneyapi.dev"

# Use GET method to retrieve data from the API and store the response in a variable
# Using the ROOT URL it will return all the characters regarding the Disney API Documentation
# Nevertheless it will return only 50 characters per default
response = requests.get(f"{ROOT_URL}/character")
print(response.status_code)

# Response headers
print(response.headers)

# Response is a JSON object, so we can use the .json() method to convert it to a Python dictionary
disney_data = response.json()
print(disney_data.keys())

# You can inspect the info key to see how many characters are available
print(disney_data["info"])
print(disney_data["data"])

# To verify the number of characters in the data key, you can use the len() function
print(len(disney_data["data"]))
# >>> 50

# To get the next page of characters, you can use the nextPage key in the info key to get the URL
print(disney_data["info"]["nextPage"])
# >>> http://api.disneyapi.dev/character?page=2&pageSize=50
response = requests.get(disney_data["info"]["nextPage"])

# Params dictionary
params = {"page": 4, "pageSize": 20}

response = requests.get(f"{ROOT_URL}/character", params=params)
characters_from_page_4_with_20_characters = response.json()

# URL with query parameters
print(response.url)
# >>> https://api.disneyapi.dev/character/character?page=4&pageSize=20

# Verify that the number of characters is 20 and the page is 4
print(characters_from_page_4_with_20_characters["info"])
# >>> {'count': 20, 'totalPages': 372, 'previousPage': 'http://api.disneyapi.dev/character?page=3&pageSize=20', 'nextPage': 'http://api.disneyapi.dev/character?page=5&pageSize=20'}

# Retrieve all information keys from the first character in the list
characters_from_page_4_with_20_characters["data"][0].keys()

# Filter only the id and the name of all characters
characters = [
    {"id": character["_id"], "name": character["name"]}
    for character in characters_from_page_4_with_20_characters["data"]
]
print(characters)

# You can also use path parameters to get specific characters with the character ID
# Path parameters are defined by curly braces in the URL
character_id = 156
response = requests.get(f"{ROOT_URL}/character/{character_id}")
character_156 = response.json()["data"]
print(character_156)

# ----

# API documentation = https://reqres.in/

# GET request to request a single fake user
BASE_URL = "https://reqres.in/api"

response = requests.get(f"{BASE_URL}/users/2")
print(response.json())


# write data with POST parameters in query string

# write data with POST (json data in body)

new_user = {"name": "New User", "job": "Data Engineer"}

# Create a new user
response = requests.post(f"{BASE_URL}/users", data=new_user)
print(response)

# Created user
print(response.json())
