import requests

url = "https://sv443.net/jokeapi/v2/joke/programming"

response = requests.get(url).json()

try:
	print(response['setup'])
	print(response['delivery'])
except:
	print(response['joke'])