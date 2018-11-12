from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
#This program creates a simple event to you google calendar with a starttime and a endtime = 1 day after you created the event

from oauth2client import file, client, tools
import datetime
import time

now = time.strftime("%c")

Current_Date_Formatted = datetime.datetime.today().strftime ('%d')  
NextDay_Date = datetime.datetime.today() + datetime.timedelta(days=1)
NextDay_Date_Formatted = NextDay_Date.strftime ('%d')

startinfo = str(time.strftime("%Y")+"-"+time.strftime("%m")+"-"+time.strftime("%d")+"T"+time.strftime("%H")+":"+time.strftime("%M")+":"+time.strftime("%S")+"-06:00")
endinfo =  str(time.strftime("%Y")+"-"+time.strftime("%m")+"-"+NextDay_Date_Formatted+"T"+time.strftime("%H")+":"+time.strftime("%M")+":"+time.strftime("%S")+"-06:00")

#startinfo and endinfo have the specified time format from the Google calendar API platform 

def createEvent(NAME):
    try:
        import argparse
        flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
    except ImportError:
        flags = None

    SCOPES = 'https://www.googleapis.com/auth/calendar'
    store = file.Storage('storage.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store, flags) \
             if flags else tools.run(flow, store)
    CAL = build('calendar', 'v3', http=creds.authorize(Http()))
    event = {
    'summary': NAME,
    'start': {'dateTime': startinfo},
    'end': {'dateTime': endinfo},
    }

    e = CAL.events().insert(calendarId='primary',
         sendNotifications=True, body=event).execute()
    eventCreated = str("EVENT: "+ NAME+ "\n"+"SUCCESSFULLY CREATED")
    return eventCreated


