import json
import requests

tokenfile = open("token.txt", "r") 
TOKEN, JUANCHAT= tokenfile.read().split()
URL = URL = "https://api.telegram.org/bot{}/".format(TOKEN)

def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return  content

def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js

def get_updates():
    url = URL + "getUpdates"
    js = get_json_from_url(url)
    return (js)

def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    name = updates["result"][last_update]["message"]["chat"]["first_name"]
    lastname = updates["result"][last_update]["message"]["chat"]["last_name"]
    return (text, chat_id, name, lastname)

def send_message(text, chat_id):
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)

def main():
    last_textchat = (None, None)
    while True:
        text, chat = get_last_chat_id_and_text(get_updates())
        if (text, chat) != last_textchat:
            send_message(text, chat)
            last_textchat = (text, chat)
        time.sleep(0.5)
    print ("Name:\t\t" + name + " " + lastname)
    print ("Chat id:\t" + str(chat_id))
    print ("Text:\t\t" + text)

if (__name__ == "__main__"):
    main()
