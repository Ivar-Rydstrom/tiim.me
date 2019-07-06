from flask import Flask, render_template, url_for, make_response, request
import datetime
import json
from event_json import eventToJson, jsonToEvents, eventToDict, dictToEvent
from event import Event


app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        form = request.form
        default_name = 0
        event = Event(
            form.get('title', default_name),
            form.get('description', default_name),
            'time',
            form.get('end_time', default_name))

        if 'events' in request.cookies:
            response = make_response(render_template('index.html'))
            events_json = request.cookies.get('events')
            events = jsonToEvents(events_json)
            events.append(eventToDict(event))
            response.set_cookie('events', json.dumps(events))
            return response

        else:
            response = make_response(render_template('index.html'))
            events = []
            events.append(eventToDict(event))
            response.set_cookie('events', json.dumps(events))
            return response

    else:
        events_json = request.cookies.get('events')
        events = jsonToEvents(events_json)
        dict = events
        return render_template('index.html', events=events)


if __name__ == '__main__':
    app.run(debug=True)
