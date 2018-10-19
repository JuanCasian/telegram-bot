import requests
import json
import random
import sys

'''
Script usage: python3 [Script_Name]
'''

TOKEN = sys.argv[1]
MESSAGE = sys.argv[2]
URL = "https://api.telegram.org/bot{}/".format(TOKEN)

def get_chat_id():
    response = requests.get("{}getupdates".format(URL))
    if (response.status_code == 200):
        data = response.json()
        return (data["result"][-1]["message"]["chat"]["id"])
    else:
        return("Unable to retrieve information")

CHAT_ID = get_chat_id()

def main():
    if (CHAT_ID != "Unable to retrieve information")
        response = requests.get("{}sendMessage?chat_id={}&text={}".format(URL, CHAT_ID, sys.argv[2]))
        if (response.status_code == 200):
            print("Message sent")
    else:
        print("Unable to retrieve information")

if __name__ == "__main__":
    main()
