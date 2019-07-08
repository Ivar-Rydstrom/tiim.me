from datetime import datetime
from event import Event


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


def strToDatetime(datetime_str):

    return

# str(datetime.datetime.now()).split('.', 1)[0]
