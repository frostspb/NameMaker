# -*- coding: utf-8 -*-

import asyncio
import os.path
import tornado.log
import tornado.web
import nmlib.srv_options  # не удалять, нужна для норм парсинга опций

from tornado.options import options
from nmlib.nm_urls import handlers
from confs.app_config import tn_settings


from confs.app_config import CONF_FILE
from nmlib.base_tornado_lib.base_tor_app import NMBaseServer

settings = tn_settings
tornado.options.parse_config_file(CONF_FILE)

# перезаписать опции, если были опции из командной строки

tornado.options.parse_command_line()


class NameGenServer(NMBaseServer):
    def __init__(self, **settings):
        super().__init__(handlers, root_dir=os.path.dirname(__file__), **settings)
        self.logger = tornado.log.gen_log
        #tornado.ioloop.IOLoop.configure('tornado.platform.asyncio.AsyncIOMainLoop')
        tornado.options.parse_config_file(CONF_FILE)
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        tornado.ioloop.IOLoop.instance().call_later(1, self.file_cleaner)

    def file_cleaner(self):
        import glob, os
        for f in glob.glob("static/*.xlsx"):
            os.remove(f)


name_maker = NameGenServer(**settings)

if __name__ == "__main__":
    name_maker.listen(options.port)


    file_cleaner = tornado.ioloop.PeriodicCallback(
        name_maker.file_cleaner, 1000*60*60*24
    )
    file_cleaner.start()
    tornado.ioloop.IOLoop.instance().start()
