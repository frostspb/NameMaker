# -*- coding: utf-8 -*-

import asyncio
import os.path
import tornado.log
import tornado.web
import nmlib.srv_options  # не удалять, нужна для норм парсинга опций

from urllib.parse import urlencode
from tornado.options import options
from nmlib.nm_urls import handlers
from confs.app_config import tn_settings


from confs.app_config import CONF_FILE
from nmlib.base_tornado_lib.base_tor_app import NMBaseServer

settings = tn_settings
tornado.options.parse_config_file(CONF_FILE)

# перезаписать опции, если были опции из командной строки

tornado.options.parse_command_line()


class WCSenderServer(NMBaseServer):
    def __init__(self, **settings):
        super().__init__(handlers, root_dir=os.path.dirname(__file__), **settings)
        self.logger = tornado.log.gen_log
        tornado.ioloop.IOLoop.configure('tornado.platform.asyncio.AsyncIOMainLoop')
        tornado.options.parse_config_file(CONF_FILE)


wc_sender_server = WCSenderServer(**settings)

if __name__ == "__main__":
    wc_sender_server.listen(options.port)
    loop = asyncio.get_event_loop()
    wc_sender_server.init_with_loop(loop)
    loop.run_forever()
    tornado.ioloop.IOLoop.instance().start()
