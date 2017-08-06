# -*- coding: utf-8 -*-
import json
import os.path
import logging.handlers
import tornado.log
import tornado.web
import aioredis
from tornado.options import options
from urllib.parse import urlencode
from tornado.httpclient import AsyncHTTPClient
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
        self.nm_debug = options.debug
        #self.redis_host = options.red
        tornado.ioloop.IOLoop.configure('tornado.platform.asyncio.AsyncIOMainLoop')
        """
        mail_logging = logging.handlers.SMTPHandler(mailhost=options.log_mail_host,
                                                    fromaddr=options.log_mail_from,
                                                    toaddrs=options.log_mail_to,
                                                    subject=options.log_mail_subj
                                                    )

        mail_logging.setLevel(logging.ERROR)

        self.logger.addHandler(mail_logging)
        """
        self.http_client = AsyncHTTPClient()


    def init_with_loop(self, loop):
        self.redis_cnt_pool = loop.run_until_complete(aioredis.create_pool(
        ('localhost', 6379),
        minsize=options.redis_min_con, maxsize=options.redis_max_con,
        loop=loop))


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

    async def get_open_url(self, url):
        """
        Делает http запрос, ответ либо json либо xml
        :param url: урл
        :param type_resp: тип ответа
        :return: словарь
        """

        res = await self.http_client.fetch(url)
        res_s = res.body.decode(encoding="utf-8")
        res_json = json.loads(res_s)
        res_wc = res_json
        return res_wc

    async def post_open_url(self, url, body):
        """
        Делает http post запрос
        :param url: урл
        :param body: словарь с пост-параметрами
        :return: словарь
        """
        headers = None
        param_s = urlencode(body)

        res = await self.http_client.fetch(url, method='POST', body=param_s, headers=headers)

        res_s = res.body.decode(encoding="utf-8")
        res_json = json.loads(res_s)

        return res_json

    async def set_redis_exp_val(self, key, val, exp, conver_to_json=False):
        if conver_to_json:
            val = json.dumps(val)

        with await self.redis_cnt_pool as redis:
            await redis.connection.execute('set', key, val)
            await redis.connection.execute('expire', key, exp)

    async def del_redis_val(self, key):
        with await self.redis_cnt_pool as redis:
            await redis.connection.execute('del', key)


    async def get_redis_val(self, key, from_json=True):
        """
            Достать инфу из редиса
        """
        try:

            with await self.redis_cnt_pool as redis:
                r = await redis.connection.execute('get', key)
                redis_val = r.decode('utf-8')
                if redis_val:
                    res = json.loads(redis_val) if from_json else redis_val
                else:
                    res = None


                return res
        except:
            self.log_exc('get_redis_val failed key = %s' % key)
            res = None
            return res







