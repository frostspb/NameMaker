# -*- coding: utf-8 -*-
import json

try:
    from bson import json_util
except:
    json_util = False
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
        print(msg)
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

    async def get_open_url(self, url):
        """
		Делает http запрос, ответ либо json либо xml
		:param url: урл
		:param type_resp: тип ответа
		:return: словарь
		"""

        return await self.application.get_open_url(url)

    async def post_open_url(self, url, body):
        """
		Делает http post запрос
		:param url: урл
		:param body: словарь с пост-параметрами
		:return: словарь
		"""
        return await self.application.post_open_url(url, body)

    async def set_redis_exp_val(self, key, val, exp, conver_to_json=False):
        if conver_to_json:
            if json_util:
                val = json.dumps(val, default=json_util.default)
            else:
                val = json.dumps(val)

        with await self.application.redis_cnt_pool as redis:
            await redis.connection.execute('set', key, val)
            await redis.connection.execute('expire', key, exp)

        return True

    async def del_redis_val(self, key):

        with await self.application.redis_cnt_pool as redis:
            await redis.connection.execute('del', key)

        return True

    async def get_redis_val(self, key, from_json=True, mail_label=''):
        """
		    Достать инфу из редиса
		"""
        try:

            with await self.application.redis_cnt_pool as redis:
                r = await redis.connection.execute('get', key)
                redis_val = r.decode('utf-8') if r is not None else r
                if redis_val:
                    if json_util:
                        res = json.loads(redis_val, object_hook=json_util.object_hook) if from_json else redis_val
                    else:
                        res = json.loads(redis_val) if from_json else redis_val
                else:

                    res = None

                return res
        except:
            self.log_exc('get_redis_val failed key = %s label=%s' % (key, mail_label))
            res = None
            return res
