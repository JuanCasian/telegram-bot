import requests
import json
import random

def main():

    #response = requests.get("https://api.telegram.org/bot717762374:AAGsntUP75OQV07HlToboFTZSaNef4M4i58/getme")
    #Api to retrieve your bot's information
    response = requests.get("https://api.telegram.org/bot717762374:AAGsntUP75OQV07HlToboFTZSaNef4M4i58/getupdates")
    #API to retrieve received messages
    if (response.status_code == 200):
        data = response.json()
        #print(*data, sep='\n')
        #You can use this notation to print all elements inside lists/directories
        #to avoid getting lost
        print(data["result"][-1]["message"]["text"])
        #printing last received message
    else:
        print("Unable to retrieve information")

if __name__ == "__main__":
    main()
