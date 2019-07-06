from flask import Flask, render_template, url_for, make_response, request


class Event:

    def __init__(self, title, description, created_time, end_time):
        self.title = title
        self.description = description
        self.created_time = created_time
        self.end_time = end_time
