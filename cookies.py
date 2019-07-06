from flask import Flask, render_template, url_for, make_response, request




def getCookie(name):
    cookie = request.cookies.get(name)
    return cookie
