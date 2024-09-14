from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

import os
import json


def create_google_event(task):
    creds = Credentials.from_authorized_user_file("credentials.json")
    service = build("calendar", "v3", credentials=creds)

    event = {
        "summary": task.title,
        "description": task.description,
        "start": {
            "dateTime": f"{task.date}T{task.time}",
            "timeZone": "UTC",
        },
        "end": {
            "dateTime": f"{task.date}T{task.time}",
            "timeZone": "UTC",
        },
    }
