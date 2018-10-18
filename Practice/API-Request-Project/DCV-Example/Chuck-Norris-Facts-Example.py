import requests
import json
import random

def main():

    response = requests.get("https://api.chucknorris.io/jokes/random")
    if (response.status_code == 200):
        data = response.json()
        print("Chuck Norris random fact #" + str(random.randint(1, 999)) + ": ")
        print(data["value"] + '\n')
    else:
        print("Unable to retrieve information")

if __name__ == "__main__":
    main()
