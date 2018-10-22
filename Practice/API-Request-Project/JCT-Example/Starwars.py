import requests
import json
import random

#This function planet will return the name of planet depending on the character selected
def planet(nameofplanet):
    planetname= ''
    response = requests.get(nameofplanet)
    if (response.status_code==200):
        data = response.json()
        planetname = str(data["name"])
    else:
        planetname = "error in planet"
    return planetname

def main():
   
    randomgenerated = random.randint(1,100)
    apilink="https://swapi.co/api/people/"+ str(randomgenerated) +"/"
    response = requests.get(apilink)
  
    if (response.status_code == 200):
        data = response.json()
        print("Character displayed is number "+ str(randomgenerated))
        print("Name " + str(data["name"]))
        print("Height " + str(data["height"]))
#We use the function planet, otherwise it would display only an api link
        print("From homeworld " + planet(str(data["homeworld"])))
    else:
        print("Error in request")

if __name__ == "__main__":
    main()
