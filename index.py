
import glob
import os
import os.path
import tornado.log
import tornado.web

from tornado.options import options
from nmlib.nm_urls import handlers
from confs.app_config import tn_settings


from confs.app_config import CONF_FILE
from torskel.torskel_app import TorskelServer


settings = tn_settings

options.define("file_cleaner_cooldown", 1000*60*60*20, type=int)

tornado.options.parse_config_file(CONF_FILE)

# перезаписать опции, если были опции из командной строки

tornado.options.parse_command_line()


class NameGenServer(TorskelServer):
    def __init__(self, **settings):
        super().__init__(handlers, root_dir=os.path.dirname(__file__), **settings)
        self.logger = tornado.log.gen_log
        self.nm_debug = options.debug
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        tornado.ioloop.IOLoop.current().call_later(1, self.file_cleaner)

    def file_cleaner(self):
        try:
            for f in glob.glob( os.path.join(self.base_dir, 'static', "*.xlsx")):
                os.remove(f)
        except:
            pass


name_maker = NameGenServer(**settings)

if __name__ == "__main__":
    name_maker.listen(options.port)

    file_cleaner = tornado.ioloop.PeriodicCallback(
        name_maker.file_cleaner, options.file_cleaner_cooldown
    )
    file_cleaner.start()
    tornado.ioloop.IOLoop.current().start()
