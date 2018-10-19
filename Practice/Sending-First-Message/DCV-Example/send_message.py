import requests
import json
import random
import sys

TOKEN = sys.argv[1]

URL = "https://api.telegram.org/bot{}/".format(TOKEN)

def get_chat_id():
    response = requests.get("{}getupdates".format(URL))
    if (response.status_code == 200):
        data = response.json()
        return (data["result"][-1]["message"]["chat"]["id"])
    else:
        print("Unable to retrieve information")

def main():
    response
    print(get_chat_id())
#https://api.telegram.org/bot<your-bot-token>/sendMessage?chat_id=<chat-id>&text=TestReply
if __name__ == "__main__":
    main()
