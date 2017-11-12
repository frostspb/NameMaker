# -*- coding: utf-8 -*-

from nmlib.handlers.permut_app.permut_page import PermutHandler
from nmlib.handlers.permut_app.start_page import StartPage


handlers = [
    (r"/", StartPage),
    (r"/permut_data", PermutHandler)
]

