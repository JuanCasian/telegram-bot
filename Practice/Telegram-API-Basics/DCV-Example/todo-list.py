from dbhelper import DBHelper
from utilities import *
import time

db = DBHelper()

def handle_updates(updates):
    update = updates["result"][-1]
    text = update["message"]["text"]
    chat = update["message"]["chat"]["id"]
    items = db.get_items(chat)  
    if text == "/done":
        keyboard = build_keyboard(items)
        send_message("Select an item to delete", chat, keyboard)
    elif text in items:
        db.delete_item(text, chat)  
        items = db.get_items(chat)  
        keyboard = build_keyboard(items)
        send_message("Select an item to delete", chat, keyboard)
    elif text == "/start":
        send_message("Welcome to your personal To Do list. Send any text to me and I'll store it as an item. Send /done to remove items", chat)
    elif text != "/end":
        db.add_item(text, chat)  
        items = db.get_items(chat)    
        message = "\n".join(items)
        send_message(message, chat)
    return (True if text != "/end" else False)

def build_keyboard(items):
    keyboard = [[item] for item in items]
    reply_markup = {"keyboard":keyboard, "one_time_keyboard": True}
    return json.dumps(reply_markup)

def main():
    last_update_id = None
    boo = True
    while True:
        updates = get_updates(last_update_id)
        if (updates["result"][-1]["update_id"] != last_update_id):
            last_update_id = get_last_update_id(updates)
            boo = handle_updates(updates)
        if (boo == False):
            break
        time.sleep(0.5)

if __name__ == '__main__':
    main()
