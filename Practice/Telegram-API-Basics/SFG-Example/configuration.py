import requests

BOT_INFO = "getme"
BOT_UPDATES = "getUpdates"

def make_get_request(token, ext):
    url = "https://api.telegram.org/bot{}/".format(token)
    response = requests.get(url + ext)
    if (response.status_code != 200):
        print ("Request could not be processed. Status code: {}".format(response.status_code))
        exit()
    response = response.json()
    if (response["ok"] == False):
        print ("API response is not ok")
        exit()
    return (response["result"])

def print_bot_info(token):
    info = make_get_request(token, BOT_INFO)
    for key, value in info.items():
        print(str(key).capitalize() + ": " + str(value))

def get_token():
    print ("Please insert bot's token:")
    token = input()
    if (len(token.split()) > 1):
        print("Input is not valid")
        return (get_token())
    return (token)

def print_updates(token):
    info = make_get_request(token, BOT_UPDATES)
    for updates in info:
        print (updates["update_id"])

def main():
    token = get_token()
    print_bot_info(token)
    print_updates(token)

if __name__ == "__main__":
    main()

