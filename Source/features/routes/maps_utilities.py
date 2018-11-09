import requests
import urllib
import json
import os
import sys

KEY = "{}&key=" + os.environ["GKEY"]
DIRECTION = "https://www.google.com/maps/dir/?api=1&origin={}&destination={}&destination_place_id={}&travelmode={}"
PLACE = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?{}".format(KEY)
MAP = "https://www.google.com/maps/search/?api=1&query={},{}&query_place_id={}"
class routes:

    def __init__(self, start_id, start, end):
        self.start_id = start_id
        self.start = start
        self.end = end

    def __repr__(self):
        return("route('{}', '{}', '{}')".format(self.start_id, self.start, self.end))

def search_place(text, lat, lon): 
    text = urllib.parse.quote_plus(text)
    url = PLACE.format("name=" + text + "&location=" + str(lat) + "0," + str(lon) + "0" + "&rankby=distance")
    response = requests.get(url)
    if (response.status_code == 200):
        data = response.json()
        return (data)
    else:
        print("Invalid token or unable to retrieve information")
        (sys.exit(0))

def clean_search(data):
    places = []
    i = 0
    while i < 3:
        places.append([])
        places[i].append(data[i]["place_id"])
        places[i].append(data[i]["name"])
        places[i].append((data[i]["vicinity"])
        places[i].append(data[i]["geometry"]["location"]["lat"])
        places[i].append(data[i]["geometry"]["location"]["lng"])
        places[i].append(MAP.format(places[i][3], places[i][4], places[i][0]))
        i += 1
    return (places)

def  get_route(start, end, method):
    url = DIRECTIONS.format
