import requests

import Config

url = "https://github.com/genedeh"
headers = {
    "Authorization": "Bearer " + Config.api_key
}
response = requests.get(url, headers=headers)
print(response)
