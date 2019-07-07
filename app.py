from flask import Flask, render_template, url_for, make_response, request, redirect
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
            events_json = request.cookies.get('events')
            events = jsonToEvents(events_json)
            events.append(eventToDict(event))
            response = make_response(redirect('/'))
            response.set_cookie('events', json.dumps(events))
            return response

        else:
            events = []
            events.append(eventToDict(event))
            response = make_response(render_template('index.html', events=events))
            response.set_cookie('events', json.dumps(events))
            return response

    else:
        if 'events' in request.cookies:
            events_json = request.cookies.get('events')
            events = jsonToEvents(events_json)
            return render_template('index.html', events=events)

        else:
            return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
