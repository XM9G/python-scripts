import requests

userid =input('Discord User Id: ')
result = requests.get('https://api.lanyard.rest/v1/users/' +userid)

user = result["username"]
print("Account: {}".format (user))