from googleapiclient.discovery import build
import datetime
from google.oauth2 import service_account
import pytz
from notify_run import Notify


def checkCalendar(cal_ID):
    SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
    SERVICE_ACCOUNT_FILE = '../config.json'

    tz = pytz.timezone('Europe/London')

    timeMin = datetime.datetime.now(tz)
    if timeMin.hour > 11:
        timeMin += datetime.timedelta(days=1)

    timeMin = timeMin.replace(hour=8, minute=30)
    timeMax = timeMin.replace(hour=10, minute=30)

    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    service = build('calendar', 'v3', credentials=credentials)

    page_token = None
    while True:
        events = service.events().list(calendarId=cal_ID, timeMin=timeMin.isoformat(), timeMax=timeMax.isoformat(),
                                       pageToken=page_token).execute()
        if len(events['items']) > 0:
            return True

        page_token = events.get('nextPageToken')
        if not page_token:
            break
    return False


def pingPhone(endpoint):
    notify = Notify(endpoint=endpoint)
    notify.send("Pre 10.30 meeting, don't be late!")
