from googleapiclient.discovery import build
from api.google_auth import get_credentials

def fetch_calendar_events(max_results=10):
    creds = get_credentials()
    service = build('calendar', 'v3', credentials=creds)
    events_result = service.events().list(calendarId='primary', maxResults=max_results,
                                          singleEvents=True, orderBy='startTime').execute()
    events = events_result.get('items', [])
    return [(e['summary'], e['start'].get('dateTime', e['start'].get('date'))) for e in events]

def add_calendar_event(summary, start_time, end_time):
    creds = get_credentials()
    service = build('calendar', 'v3', credentials=creds)
    event = {
        'summary': summary,
        'start': {'dateTime': start_time, 'timeZone': 'UTC'},
        'end': {'dateTime': end_time, 'timeZone': 'UTC'}
    }
    created_event = service.events().insert(calendarId='primary', body=event).execute()
    return created_event.get('htmlLink')
