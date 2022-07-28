import requests

username = input("Username/Id: ")

result = requests.get("http://api.whatpulse.org/user.php?user=" + username +"&formatted=yes&format=json").json()

if 'error' in result:
    print("Something went wrong: ", result['error'])
else:
    keys = result["Keys"]
    clicks = result["Clicks"]
    usernameresult =result["AccountName"]


    print("""
    ██╗    ██╗██╗  ██╗ █████╗ ████████╗██████╗ ██╗   ██╗██╗     ███████╗███████╗
    ██║    ██║██║  ██║██╔══██╗╚══██╔══╝██╔══██╗██║   ██║██║     ██╔════╝██╔════╝
    ██║ █╗ ██║███████║███████║   ██║   ██████╔╝██║   ██║██║     ███████╗█████╗  
    ██║███╗██║██╔══██║██╔══██║   ██║   ██╔═══╝ ██║   ██║██║     ╚════██║██╔══╝  
    ╚███╔███╔╝██║  ██║██║  ██║   ██║   ██║     ╚██████╔╝███████╗███████║███████╗
    ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝      ╚═════╝ ╚══════╝╚══════╝╚══════╝
                                                                             """)
    print("Stats for {}".format (usernameresult))
    print("{} Keys, {} Clicks ".format(keys, clicks))

