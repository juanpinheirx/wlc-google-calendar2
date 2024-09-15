import pytest
from unittest.mock import patch, MagicMock
from datetime import datetime, time, timedelta
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from calendar_events.google_calendar import create_google_event, delete_google_event


class Task:
    def __init__(self, title, description, date, time=None):
        self.title = title
        self.description = description
        self.date = date
        self.time = time


@pytest.fixture
def task():
    return Task(
        title="Nova Tarefa",
        description="Descrição da nova tarefa",
        date=datetime(2023, 10, 1).date(),
        time=datetime(2023, 10, 1, 14, 0).time(),
    )


@patch("calendar_events.google_calendar.get_google_service")
def test_create_google_event(mock_get_google_service, task):
    mock_service = MagicMock()
    mock_get_google_service.return_value = mock_service
    mock_events = mock_service.events.return_value
    mock_insert = mock_events.insert.return_value
    mock_insert.execute.return_value = {"id": "event_id"}

    event_id = create_google_event(task)
    assert event_id == "event_id"
    mock_events.insert.assert_called_once_with(
        calendarId="primary",
        body={
            "summary": task.title,
            "description": task.description,
            "start": {
                "dateTime": f"{task.date}T{task.time}",
                "timeZone": "America/Sao_Paulo",
            },
            "end": {
                "dateTime": f"{task.date}T{(datetime.combine(task.date, task.time) + timedelta(hours=1)).time()}",
                "timeZone": "America/Sao_Paulo",
            },
        },
    )
    mock_insert.execute.assert_called_once()


@patch("calendar_events.google_calendar.get_google_service")
def test_delete_google_event(mock_get_google_service):
    mock_service = MagicMock()
    mock_get_google_service.return_value = mock_service

    event_id = "event_id"
    result = delete_google_event(event_id)
    assert result is True
    mock_service.events().delete.assert_called_once_with(
        calendarId="primary", eventId=event_id
    )
    mock_service.events().delete().execute.assert_called_once()
