import os
import logging
from cx_Oracle import makedsn
from flask import Flask
from pony.orm import *

logging.basicConfig(level=os.environ.get('LOG_LEVEL', 'DEBUG'))
log = logging.getLogger(__name__)


db = Database()
app = Flask(__name__)

_is_connected = False

_user = os.environ.get('DB_USER')
_password = os.environ.get('DB_PASSWORD')
_host = os.environ.get('DB_HOST', 'localhost')
_port = int(os.environ.get('DB_PORT', 1521))
_sid = os.environ.get('DB_SID')  # db name

log.debug("HOST: %s", _host)
log.debug("PORT: %s", _port)
log.debug("SID: %s", _sid)
log.debug("USER: %s", _user)


def _connection_checker():
    global db
    global _is_connected
    if _is_connected:
        return True, 'OK'

    conn_string = '%s/%s@%s' % (_user, _password, makedsn(_host, _port, _sid))
    # Instead of going for single connection which is pretty much resource consuming - you can always use connection pool in like below 
    # cx_Oracle.SessionPool(username,password,DB_name,min=1,max=8, timeout=300)
    #make sure you set min , max and timeout as per requirnment  
    try:
        db.bind("oracle", conn_string)
        log.info('Connected to [%s:%s]' % (_host, _port))
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
