#This program is the main of my two Google calendar API commands bot
# /checkevent + number = "retrieve the number of events you wanted to know"
# /createevent + name = "creates an event with the name you gave into your google calendar"

import json
import requests
import time
import quickstart   #This program is from the Google API for creating a event
import quickstart2  #This program is from the Google API for reading Calendar data
import findword     #This program is for finding the word after a keyword

def getToken():                              
    userinput=input("Enter Bot Token: ")     
    return userinput     
# getToken() will be used in all documents to ask for the bot's token
                                             
TOKEN =str(getToken())
URL = "https://api.telegram.org/bot{}/".format(TOKEN)
keyword1 = "/checkevent"
keyword2 = "/createevent"

def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content

def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js

def get_updates(offset=None):
    url = URL + "getUpdates"
    if offset:
        url += "?offset={}".format(offset)
    js = get_json_from_url(url)
    return js

def googleCalendar(updates):                  #Main function for my 2 commands 
    for update in updates["result"]:
         try:
            text = update["message"]["text"]
            chat = update["message"]["chat"]["id"] 
            if "/checkevent" in text.lower():
                numberEvents = findword.findWord(text, keyword1)  #Saves the number of events you want to retrieve information in numbEvents variable
                resp = quickstart2.readCalendar(numberEvents)     #Calls for the events from the Google API
                send_message(resp, chat)
            if  "/createevent" in text.lower():
                nameEvent = findword.findWord(text, keyword2)    #Saves the name of the event you wanted to create
                resp = quickstart.createEvent(nameEvent)         #Creates the event from the Google API
                send_message(resp, chat) 
         except Exception as e:
            print(e)

def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (text, chat_id)

def get_last_update_id(updates):
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    return max(update_ids)

def send_message(text, chat_id):
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)

def main():
    last_update_id = None
    while True:
        updates = get_updates(last_update_id)
        if len(updates["result"]) > 0:
            last_update_id = get_last_update_id(updates) + 1 
            googleCalendar(updates) 
        time.sleep(0.5)

if __name__ == '__main__':
    main()

