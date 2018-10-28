import APICommands as coms
import requests

SEND_MSG = "sendMessage?chat_id={}&text={}"
url = "https://api.telegram.org/bot{}/"
tokenfile = open("token.txt", "r") 
token = tokenfile.read()

def send_message(token):
    print("Enter chat id:")
    chat_id = input()
    print("Enter Reply:")
    reply = input()
    response = requests.get(url.format(token) + SEND_MSG.format(chat_id, reply))
    print(response.status_code)

def main():
    coms.print_updates(token)
    send_message(token)

if __name__ == "__main__":
    main()
