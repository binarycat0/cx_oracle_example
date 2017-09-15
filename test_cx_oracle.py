import os
import logging
from cx_Oracle import makedsn
from flask import Flask
from pony.orm import *

log = logging.getLogger(__name__)
log.addHandler(logging.StreamHandler())

db = Database()
app = Flask(__name__)

_is_connected = False


def _connection_checker():
    global db
    global _is_connected
    if _is_connected:
        return True, 'OK'

    user = os.environ.get('DB_USER')
    password = os.environ.get('DB_PASSWORD')

    host = os.environ.get('DB_HOST', 'localhost')
    port = int(os.environ.get('DB_PORT', 1521))
    sid = os.environ.get('DB_SID')  # db name

    conn_string = '%s/%s@%s' % (user, password, makedsn(host, port, sid))
    try:
        db.bind("oracle", conn_string)
        log.info('Connected to [%s:%s]' % (host, port))
    except Exception as e:
        log.exception(e)
        return False, e.message

    _is_connected = True
    return True, 'OK'


def connect(func):
    def wrapper(*args, **kwargs):
        check, msg = _connection_checker()
        if check:
            return func(*args, **kwargs)
        return '%s' % (msg,)
    return wrapper


@db_session
def _get_sysdate():
    global db
    return db.select("SELECT SYSDATE FROM dual")


@app.route("/")
@connect
def index():
    response = ""
    try:
        data = _get_sysdate()
        response = 'SYSDATE == %s' % (data[0].isoformat())
    except Exception as e:
        log.exception(e)
        return 'Some exception while select: \n%s' % (e)

    return response
