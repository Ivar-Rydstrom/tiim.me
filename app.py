from flask import Flask, render_template, url_for, make_response, request, redirect
import datetime
import json
from event_json import eventToJson, jsonToEvents, eventToDict, dictToEvent
from dates import datetimeToDict, ISOStringToDict
from event import Event


app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():

    if request.method == 'POST':  # POST method on index route
        form = request.form
        default_name = 0
        event = Event(  # create event object from form data
            form.get('title', default_name),
            form.get('description', default_name),
            ISOStringToDict(form.get('created_time', default_name)),
            ISOStringToDict(form.get('end_time', default_name))
        )

        if 'events' in request.cookies:  # if cookie allready exists
            events_json = request.cookies.get('events')
            events = jsonToEvents(events_json)
            events.append(eventToDict(event))
            response = make_response(redirect('/'))
            response.set_cookie('events', json.dumps(events))
            return response

        else:  # if cookie does not allready exist
            events = []
            events.append(eventToDict(event))
            response = make_response(redirect('/'))
            response.set_cookie('events', json.dumps(events))
            return response


    else:  # GET method on index route
        if 'events' in request.cookies:  # if cookie allready exists
            events_json = request.cookies.get('events')
            events = jsonToEvents(events_json)
            return render_template('index.html', events=events)

        else:  # if cookie does not allready exist
            return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=False)
