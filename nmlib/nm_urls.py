# -*- coding: utf-8 -*-

from nmlib.handlers.permut_app.permut_page import PermutHandler
from nmlib.handlers.permut_app.start_page import StartPage
from nmlib.handlers.permut_app.xls_export import XlsPage

# урлы, которые обрабатываем (как urls.py в Django
handlers = [
    (r"/", StartPage),
    (r'/xls', XlsPage),
    (r"/permut_data", PermutHandler)
]

# много урлов
#handlers.extend(more_handlers)
