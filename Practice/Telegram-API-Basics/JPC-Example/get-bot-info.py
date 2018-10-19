import requests

def retrieve_bot_info(token):
    response = requests.get("https://api.telegram.org/bot{}/getme".format(token))
    if (response.status_code == 200):
        return (response.json())
    print ("Request could not be processed")
    exit()

def print_bot_info(info):
    print (info)

def main():
    print ("Please insert bot's token:")
    token = input()
    if (len(token.split()) > 1):
        print("Input is not valid")
        exit()
    info = retrieve_bot_info(token)
    print_bot_info(info)

if __name__ == "__main__":
    main()


