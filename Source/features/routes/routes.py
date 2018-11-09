from utilities import *
from maps_utilities import *
import emoji

route = routes(None, None, None)
places = []
done = False
transportation =[[emoji.emojize(":blue_car:", use_aliases=True), emoji.emojize(":bicyclist:", use_aliases=True)], [emoji.emojize(":runner:", use_aliases=True), emoji.emojize(":bus:", use_aliases=True)]] 
t = [emoji.emojize(":blue_car:", use_aliases=True), emoji.emojize(":bicyclist:", use_aliases=True), emoji.emojize(":runner:", use_aliases=True), emoji.emojize(":bus:", use_aliases=True), "driving", "bicycling", "walking", "transit"]

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
            if len(places) == 4 and text != ("/end" or "Cancel"):
                i = 0 
                while i < 3:
                    if text == keyboard[i]:
                        places = places[i]
                        send_message("Select a transportation method:", chat, build_keyboard(transportation))
                        i += 1
                        return
            elif len(places) == 5 and text != ("/end" or "Cancel"):
                method = t[t.index[text] + 4]
                link = get_route(route.start, places, method)
                send_message(link, chat)
                done = True
                return
            elif text == ("/end" or "Cancel"):
                return
            else:
                data = search_place(text, route.start["latitude"], route.start["longitude"])
                places = clean_search(data["results"])
                i = 0
                keyboard = []
                while i < 3:
                    keyboard.append(places[i][1] + ", "+ places[i][2])
                    i += 1
                keyboard.append("Cancel")
                send_message("Select your location:", chat, keyboard)
                i = 0
                while i < 3:
                    send_message(data[i][4], chat)
                    i += 1
                    return
    elif location is not None:
        send_message("Where are you going?", chat, json.dumps({"remove_keyboard": True}))

         
def main():
    last_update_id = None
    while done == False:
        updates = get_updates(last_update_id)
        if (updates["result"][-1]["update_id"] != last_update_id):
            last_update_id = get_last_update_id(updates)
            manage_route(updates)
        if "text" in updates["result"][-1]["message"]:
            if updates["result"][-1]["message"]["text"] == "/end" or "Cancel":
                break


if __name__ == '__main__':
    main()
