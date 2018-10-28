import json
import requests
import ReadingMessage 

TOKEN =str(ReadingMessage.getToken())
URL = "https://api.telegram.org/bot{}/".format(TOKEN)
                           
 
  #The result is a list of updates with a bunch of data about the sender   
response = requests.get("https://api.telegram.org/bot"+TOKEN+"/getUpdates") 
if (response.status_code == 200):
	data = response.json ()
	print("Information of API Request")
	print(data)
else:
	print("Error")
   
if __name__ =='__main_':
	main()
