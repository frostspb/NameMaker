# -*- coding: utf-8 -*-

from tornado.options import define, options

options.define("file_cleaner_cooldown", 1000*60*60*20, type=int)
options.define("secret_key", '4t=+u0_bt7#xwf*8arxb#h3!0-h6-ed44(2#5#+kkg!jrq33!#', type=str)