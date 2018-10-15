import requests
import json

def main():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    print(response.status_code)

if __name__== "__main__":
    main()
