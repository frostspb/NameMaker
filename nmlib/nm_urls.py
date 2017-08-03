# -*- coding: utf-8 -*-

from nmlib.handlers.index_page.view import IndexPage, PermutHandler



# урлы, которые обрабатываем (как urls.py в Django
handlers = [
    (r"/", IndexPage),

    (r"/permut_data", PermutHandler)
]

# много урлов
#handlers.extend(more_handlers)
