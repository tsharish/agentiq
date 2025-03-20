from typing import Annotated
from operator import itemgetter

from .data import events


def get_events_by_date(date: Annotated[str, "Date of the event, formatted as YYYY-MM-DD"]):
    """Returns all events in a given date"""
    events[0]["date"] = events[1]["date"] = events[2]["date"] = date
    day_events = [event for event in events if event["date"] == date]
    return sorted(day_events, key=itemgetter("start_time"))


def create_event(
    name: Annotated[str, "Name of the event"],
    date: Annotated[str, "Date of the event, formatted as YYYY-MM-DD"],
    start_time: Annotated[str, "Start time of the event, formatted as HH:MM"],
    end_time: Annotated[str, "End time of the event, formatted as HH:MM"],
):
    """Creates a new event based on event name, date, start and end time"""
    new_event = {"name": name, "date": date, "start_time": start_time, "end_time": end_time}
    events.append(new_event)
    return f"Event '{name}' created successfully for {date} from {start_time} to {end_time}"
