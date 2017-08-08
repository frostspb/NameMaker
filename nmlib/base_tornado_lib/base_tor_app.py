# -*- coding: utf-8 -*-
import json
import os.path

import tornado.log
import tornado.web

from tornado.options import options
from urllib.parse import urlencode

from confs.app_config import DEBUG

LOG_MSG_DEBUG_TMPL = ' %s %s'

settings = {
    'cookie_secret': options.secret_key,
    'xsrf_cookies': True,
}


class NMBaseServer(tornado.web.Application):
    def __init__(self, handlers, root_dir, **settings):
        super().__init__(handlers, static_path=os.path.join(root_dir, "static"),
                         template_path=os.path.join(root_dir, "templates"),
                         **settings)


        self.logger = tornado.log.gen_log
        self.nm_debug = False#options.debug
        #self.redis_host = options.red
        #tornado.ioloop.IOLoop.configure('tornado.platform.asyncio.AsyncIOMainLoop')


    def get_log_msg(self, msg, grep_label=''):
        """
        Собирает соощение по шаблону
        :param msg: сообщение
        :param grep_label: метка для грепанья
        :return: итоговое сообщение
        """
        try:
            res = LOG_MSG_DEBUG_TMPL % (grep_label, msg)
        except Exception:
            res = msg
        return res

    def log_debug(self, msg, grep_label=''):
        """
        Дебаг лог
        :param msg: сообщение
        :param grep_label: метка для грепанья
        :return:
        """
        self.logger.debug(self.get_log_msg(msg, grep_label))

    def log_err(self, msg, grep_label=''):
        """
        Логирует ошибку
        :param msg: сообщение
        :param grep_label: метка для грепанья
        :return:
        """
        self.logger.error(self.get_log_msg(msg, grep_label))

    def log_exc(self, msg, grep_label=''):
        """
        Логирует исключение
        :param msg: сообщение
        :param grep_label: метка для грепанья
        :return:
        """
        self.logger.exception(self.get_log_msg(msg, grep_label))






