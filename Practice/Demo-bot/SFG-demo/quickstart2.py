#This program retrieves the number of events you want from your google calendar account

from __future__ import print_function
import datetime
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

def readCalendar(number):
    SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('calendar', 'v3', http=creds.authorize(Http()))

    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    print('Getting the upcoming', number, 'events')
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                        maxResults=number, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])

    anstime  = []
    ansevent = []

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        anstime.append(start)
        ansevent.append(event['summary'])

        ans = ("TIME: "+str(anstime)+ "\n" +"EVENT: "+str(ansevent))

    return ans

