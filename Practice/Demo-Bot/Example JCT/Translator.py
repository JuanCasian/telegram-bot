import json
import requests
import time
import dbhelper
#format: translate word/ to language
# getToken() will be used in all documents to ask for the bot's token instead of including it directly in code
def getToken():                              
    userinput=input("Enter Bot Token: ")     
    return userinput                             
                                             
TOKEN =str(getToken())
URL = "https://api.telegram.org/bot{}/".format(TOKEN)


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

def translator(updates):
    for update in updates["result"]:
        try:
            text = update["message"]["text"]
            chat = update["message"]["chat"]["id"]
            targetlanguage='de'
            resp=dbhelper.traductor(text)
            if "translate" in text.lower():
                send_message(resp,chat)
            else:
               send_message("could not understand command", chat)
           # send_message(resp,chat)
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
            translator(updates)
        time.sleep(0.5)

if __name__ == '__main__':
    main()

