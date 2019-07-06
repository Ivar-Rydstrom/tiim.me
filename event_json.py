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


def jsonToEvent(json_data):
    dict = json.loads(json_data)
    event = Event(
        dict['name'],
        dict['discription'],
        dict['created_time'],
        dict['end_time'])
    return event
