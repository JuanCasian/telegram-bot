from utilities import *
import time

def main():
    last_update_id = None
    while True:
        updates = get_updates(last_update_id)
        if (updates["result"][-1]["update_id"]) != last_update_id:
            text, chat_id = get_last_chat_id_and_text(updates)
            send_message(text, chat_id)
            last_update_id = get_last_update_id(updates)
        time.sleep(.5)

if __name__ == '__main__':
    main()
