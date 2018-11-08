import requests
import urllib
import json
import sys
import os

TOKEN = os.environ["TTOK"]
URL = "https://api.telegram.org/bot{}/".format(TOKEN)

def get_updates(offset=None):
    url = URL + "getUpdates?timeout=100";
    if (offset):
        url += "?offset={}".format(offset)
    response = requests.get(url)
    if (response.status_code == 200):
        data = response.json()
        return (data)
    else:
        print("Invalid token or unable to retrieve information")
        (sys.exit(0))

def get_last_update_id(updates):
    return (int(updates["result"][-1]["update_id"]))

def get_last_chat_id_and_text(updates):
    text = updates["result"][-1]["message"]["text"]
    chat_id = updates["result"][-1]["message"]["chat"]["id"]
    return (text, chat_id)

def send_message(text, chat_id, reply_markup=None):
    text = urllib.parse.quote_plus(text)
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    if reply_markup:
        url += "&reply_markup={}".format(reply_markup)
    requests.get(url)

def build_simple_keyboard(items):
    keyboard = [[item] for item in items]
    reply_markup = {"keyboard":keyboard, "one_time_keyboard": True}
    return json.dumps(reply_markup)

def build_keyboard(keyboard):
    reply_markup = {"keyboard":keyboard, "one_time_keyboard": True}
    return json.dumps(reply_markup)
