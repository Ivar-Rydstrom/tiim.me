from flask import Flask, render_template, url_for, make_response, request
import datetime
import json
from event_json import eventToJson, jsonToEvent
from event import Event
from cookies import getCookie


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
            form.get('end_date', default_name))
        response = make_response(render_template('index.html'))
        response.set_cookie('event', eventToJson(event))
        return response

    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
