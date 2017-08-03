# -*- coding: utf-8 -*-

import socket
import os

tn_settings = {
	"cookie_secret": "61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
	"login_url": "/login",
}

PERIOD_PAY_REPEATER = 1000*60*120  # 120 минут

DEBUG = True

DEV_SRV = ['scy-core-l']

srv = socket.gethostname()
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

REDS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_MIN_CON = 50 if srv in DEV_SRV else 300
REDIS_MAX_CON = 100 if srv in DEV_SRV else 700

CONF_PROD_FIlE = 'server_conf_prod.py'
CONF_DEV_FIlE = 'server_conf_dev.py'

if srv in DEV_SRV:
	CONF_FILE = os.path.join(BASE_DIR, 'confs', CONF_DEV_FIlE)
else:
	CONF_FILE = os.path.join(BASE_DIR, 'confs', CONF_PROD_FIlE)

