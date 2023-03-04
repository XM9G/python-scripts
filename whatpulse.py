import requests

username = input("Username/Id: ")

result = requests.get("http://api.whatpulse.org/user.php?user=" + username +"&formatted=yes&format=json").json()

if 'error' in result:
    print("Something went wrong: ", result['error'])
else:
    keys = result["Keys"]
    clicks = result["Clicks"]
    usernameresult =result["AccountName"]
    download =result["Download"]
    upload =result["Upload"]
    uptime =result["UptimeLong"]


    print("""
    ██╗    ██╗██╗  ██╗ █████╗ ████████╗██████╗ ██╗   ██╗██╗     ███████╗███████╗
    ██║    ██║██║  ██║██╔══██╗╚══██╔══╝██╔══██╗██║   ██║██║     ██╔════╝██╔════╝
    ██║ █╗ ██║███████║███████║   ██║   ██████╔╝██║   ██║██║     ███████╗█████╗  
    ██║███╗██║██╔══██║██╔══██║   ██║   ██╔═══╝ ██║   ██║██║     ╚════██║██╔══╝  
    ╚███╔███╔╝██║  ██║██║  ██║   ██║   ██║     ╚██████╔╝███████╗███████║███████╗
    ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝      ╚═════╝ ╚══════╝╚══════╝╚══════╝
                                                                             """)
    print("Stats for {}".format (usernameresult))
    print("")
    print("Input Stats:")
    print("{} Keys, {} Clicks ".format(keys, clicks))
    print('')
    print('Network Stats')
    print("{} Download, {} Upload".format(download, upload))
    print('')
    print('Uptime Stats')
    print('{} Uptime'.format(uptime))
    input()