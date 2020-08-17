import requests

while True:
	try:
		emoji_name = input("Enter emoji name: ")

		url = "https://emoji-api.com/emojis?search="+emoji_name+"&access_key={your_api_key}"

		response = requests.get(url).json()


		for i in response:
		    print(i['slug'], end="\n ")
		    print(i['character'])
	except TypeError:
		print("\n emoji not found ...! \n")
	except Exception:
		print("\n Opps ! please check your network and try again ..! \n")
	else:
		break