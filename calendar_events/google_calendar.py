from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import os
import google.auth
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
import pickle
from datetime import datetime, timedelta

SCOPES = ["https://www.googleapis.com/auth/calendar"]


def get_google_service():
    creds = None

    parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    credentials_path = os.path.join(parent_dir, "credentials.json")

    if os.path.exists("token.pickle"):
        try:
            with open("token.pickle", "rb") as token:
                creds = pickle.load(token)
            print("Arquivo token.pickle carregado com sucesso.")
        except Exception as e:
            print(f"Erro ao carregar o arquivo token.pickle: {e}")

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(credentials_path, SCOPES)
            creds = flow.run_local_server(port=8000)
        try:
            with open("token.pickle", "wb") as token:
                pickle.dump(creds, token)
            print("Arquivo token.pickle criado com sucesso.")
        except Exception as e:
            print(f"Erro ao criar o arquivo token.pickle: {e}")

    service = build("calendar", "v3", credentials=creds)
    return service


def create_google_event(task):
    service = get_google_service()

    duration = timedelta(hours=1)

    if task.time:
        start_datetime = datetime.combine(task.date, task.time)
    else:
        start_datetime = datetime.combine(task.date, datetime.min.time())

    end_datetime = start_datetime + duration

    event = {
        "summary": task.title,
        "description": task.description,
        "start": {
            "dateTime": start_datetime.isoformat(),
            "timeZone": "America/Sao_Paulo",
        },
        "end": {
            "dateTime": end_datetime.isoformat(),
            "timeZone": "America/Sao_Paulo",
        },
    }

    event = service.events().insert(calendarId="primary", body=event).execute()
    return event["id"]


def delete_google_event(event_id):
    service = get_google_service()

    service.events().delete(calendarId="primary", eventId=event_id).execute()
    return True
