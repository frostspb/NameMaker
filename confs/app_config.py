# -*- coding: utf-8 -*-

import socket
import os

tn_settings = {
    "cookie_secret": "61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
    "login_url": "/login",
}

DEBUG = False

DEV_SRV = ['scy-core-l']

srv = socket.gethostname()
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


MAX_GEN_RECORDS = 100000
MAX_EXC_RECORDS = 100000

MAX_GRID_W = 20
MAX_GRID_H = 100

DEFAULT_GRID_W = 3
DEFAULT_GRID_H = 3
DEFAULT_RECORDS_COUNT = 200

CONF_PROD_FIlE = 'server_conf_prod.py'
CONF_DEV_FIlE = 'server_conf_dev.py'

if srv in DEV_SRV:
    CONF_FILE = os.path.join(BASE_DIR, 'confs', CONF_DEV_FIlE)

else:
    CONF_FILE = os.path.join(BASE_DIR, 'confs', CONF_PROD_FIlE)
