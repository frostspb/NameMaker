# -*- coding: utf-8 -*-

from tornado.options import define, options

options.define('debug', default=True, help='debug mode', type=bool)
options.define("port", default=8006, help="run on the given port", type=int)
options.define("log_mail_subj", default='nm log', type=str)
options.define("log_mail_from", default='***@***.ru', type=str)
options.define("log_mail_to", default=['*@***.ru'], type=list)
options.define("redis_min_con", default=50, type=int)
options.define("redis_max_con", default=100, type=int)
options.define("log_mail_host", default='*', type=str)
options.define("secret_key", '4t=+u0_bt7#xwf*8arxb#h3!0-h6-ed44(2#5#+kkg!jrq33!#', type=str)