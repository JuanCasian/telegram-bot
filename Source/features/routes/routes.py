from utilities import *
from maps_utilities import *

route = routes(None, None, None)

def  manage_route(updates):
    update = updates["result"][-1]
    chat = update["message"]["chat"]["id"]
    if "text" in update["message"]:
        text = update["message"]["text"]
    else:
        text = None
    if "location" in update["message"]:
        location = update["message"]["location"]
        if route.start is None:
            route.start = location
            route.start_id = get_last_update_id(updates)
    else:
        location = None
    if text is not None:
        if text == "/route" and route.start == None:
            keyboard = build_keyboard([[{"text": "Yes", "request_location": True}], ["No"], ["Cancel"]])
            send_message("Start route from current location?", chat, keyboard)
        elif route.start is not None:
            if text == "/end":
                return
            else:
                data = search_place(text, route.start["latitude"], route.start["longitude"])
                data = clean_search(data["results"])
                print(*places, sep='\n')
    elif location is not None:
        if route.start == location:
            if route.start_id == get_last_update_id(updates):
                send_message("Where are you going?", chat, json.dumps({"remove_keyboard": True}))

         
def main():
    last_update_id = None
    while True:
        updates = get_updates(last_update_id)
        if (updates["result"][-1]["update_id"] != last_update_id):
            last_update_id = get_last_update_id(updates)
            manage_route(updates)
        if "text" in updates["result"][-1]["message"]:
            if updates["result"][-1]["message"]["text"] == "/end":
                break


if __name__ == '__main__':
    main()
