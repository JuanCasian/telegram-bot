import requests
import json

def main():
    response = requests.get("https://api.tronalddump.io/random/quote")
    if (response.status_code ==200):
        data = response.json()
        print("Donald Trump said on " + data["appeared_at"] + " :")
        print(data["value"])
    else:
        print("Unable to retrive information")

if __name__ == "__main__":
    main()
