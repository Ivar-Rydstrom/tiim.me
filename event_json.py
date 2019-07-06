from event import Event
import json


def eventToJson(event):
    dict = {
        'title': event.title,
        'description': event.description,
        'created_time': event.created_time,
        'end_time': event.end_time
    }
    return json.dumps(dict)


def eventToDict(event):
    dict = {
        'title': event.title,
        'description': event.description,
        'created_time': event.created_time,
        'end_time': event.end_time
    }
    return dict


def jsonToEvents(json_data):
    events = json.loads(json_data)
    return events


def dictToEvent(dict):
    event = Event(
        dict['name'],
        dict['discription'],
        dict['created_time'],
        dict['end_time'])
    return event
