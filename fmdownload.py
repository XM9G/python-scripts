import json
import webbrowser
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0'}

# load the JSON file
with open("FavoriteMedia.config.json", "r") as f:
    data = json.load(f)

# iterate through the URLs
for media in data["image"]["medias"]:
    url = media["url"]
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        # Open the URL in the default web browser
        webbrowser.open(url)
    else:
        print(f"Error {response.status_code} occured while trying to access {url}")
