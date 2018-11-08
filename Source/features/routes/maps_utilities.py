import requests
import urllib
import json
import os
import sys

KEY = "{}&key=" + os.environ["GKEY"]
DIRECTION = "https://maps.googleapis.com/maps/api/directions/json?{}".format(KEY)
PLACE = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?{}".format(KEY)

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

def clean_search(text, data):
    places = [[]]
    i = 0
    
    while i < 5:
        places[i].append(data[i]["id"])
        places[i].append(data[i]["name"])
        places[i].append(data[i]["vicinity"])
        i += 1
