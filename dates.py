from datetime import datetime
from event import Event
import re

def datetimeToDict(_datetime):
    dict = {
        'year': _datetime.year,
        'month': _datetime.month,
        'day': _datetime.day,
        'hour': _datetime.hour,
        'minute': _datetime.minute,
        'second': _datetime.second
    }
    return dict


def dictToDatetime(dict):
    _datetime = datetime(
        dict['year'],
        dict['month'],
        dict['day'],
        dict['hour'],
        dict['minute'],
        dict['second']
    )
    return _datetime


def ISOStringToDict(ISOString):
    splits = re.split('[-T:]', ISOString)
    dict = {
        'year': splits[0],
        'month': splits[1],
        'day': splits[2],
        'hour': splits[3],
        'minute': splits[4],
        'second': '0'
    }
    return dict
