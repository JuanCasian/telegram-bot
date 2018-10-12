import requests
import json

def main():
    '''
    This is a simple get request
    response = requests.get("http://api.open-notify.org/iss-now.json")
    print(response.status_code)
    '''
    response = requests.get("http://api.open-notify.org/astros.json")
    # it is important to always check the status code before doing anythin to
    # the information
    if (response.status_code == 200):
        data = response.json()
        print("Number of people in space: " + str(data["number"]))
        print("Names:")
        for person in data["people"]:
            print(person["name"])
    else:
        print("Error in request")

if __name__ == "__main__":
    main()
