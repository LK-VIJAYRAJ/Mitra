from googleapiclient.discovery import build
from api.google_auth import get_credentials
import base64
import email

def fetch_recent_emails(max_results=5):
    creds = get_credentials()
    service = build('gmail', 'v1', credentials=creds)
    results = service.users().messages().list(userId='me', maxResults=max_results).execute()
    messages = results.get('messages', [])

    email_summaries = []
    for msg in messages:
        msg_data = service.users().messages().get(userId='me', id=msg['id']).execute()
        payload = msg_data.get('payload', {})
        headers = payload.get('headers', [])
        subject = next((h['value'] for h in headers if h['name'] == 'Subject'), 'No Subject')
        email_summaries.append(subject)
    return email_summaries
