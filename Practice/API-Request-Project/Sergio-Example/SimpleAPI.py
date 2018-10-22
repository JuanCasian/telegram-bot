#Sergio Garcia 
#October 21, 2018
#API request to http://numbersapi.com/random/year?json

import requests
import json 
import random

def main():
    type = ["trivia", "year", "date", "math"]
    randomtype = type[(random.randint(0,3))]
    randomnumber =str(random.randint(1,9999))
    
 #Random numbers and random types for the API

    response = requests.get("http://numbersapi.com/"+ randomnumber + "/" + randomtype + "?json")
    if (response.status_code == 200):
        data = response.json ()
        print("Information of API Request")
        print("Number: "+str(data["number"]))
        print("Type: " +str(data["type"]))
        print("Text: "+str(data["text"]))
    else:
        print("Error")
      
if __name__ == "__main__":
    main()
