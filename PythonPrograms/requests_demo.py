import json
import requests 
import sys


if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&lmit=1&term=weezer")
print(response.json())