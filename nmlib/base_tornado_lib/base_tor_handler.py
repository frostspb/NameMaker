# -*- coding: utf-8 -*-

import tornado.gen
from tornado.options import options
import hashlib


class NMBaseHandler(tornado.web.RequestHandler):
    def __init__(self, application, request, **kwargs):
        super(NMBaseHandler, self).__init__(application, request, **kwargs)
        self.nm_debug = self.application.nm_debug
        self.user_l = self.get_cookie('cur_lang', 'ru')

    def get_hash_str(self, value, alg='sha224'):
        res = None

        try:
            if isinstance(value, str):
                res = getattr(hashlib, alg)(value.encode('utf-8')).hexdigest()
        except:
            pass

        return res

    def get_req_args(self, args_list=None):
        """
		Забирает из реквеста список параметров
		:param args_list: список параметров
		:return: список значений параметров
		"""
        if not args_list:
            args_list = []
        return [self.get_argument(x, False) for x in args_list]

    def _handle_request_exception(self, e):
        super(NMBaseHandler, self)._handle_request_exception(e)
        msg = '''handler classname = %s \n
			   request = %s \n
		       exception = %s\n'''

        self.log_exc(msg % (type(self).__name__, self.request, e))

    def get_current_user(self):
        return self.get_secure_cookie("user")

    def log_debug(self, msg, grep_label=''):
        """
		Дебаг лог
		:param msg: сообщение
		:param grep_label: метка для грепанья
		:return:
		"""
        
        self.application.log_debug(msg, grep_label=grep_label)

    def log_err(self, msg, grep_label=''):
        """
		Логирует ошибку
		:param msg: сообщение
		:param grep_label: метка для грепанья
		:return:
		"""
        self.application.log_err(msg, grep_label=grep_label)

    def log_exc(self, msg, grep_label=''):
        """
		Логирует исключение
		:param msg: сообщение
		:param grep_label: метка для грепанья
		:return:
		"""
        self.application.log_exc(msg, grep_label)
