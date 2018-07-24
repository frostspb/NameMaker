import sys
import os.path
import tornado.options

from tornado.options import options
from tornado.testing import AsyncHTTPTestCase
from index import name_maker

APP_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(os.path.join(APP_ROOT, '..'))

tornado.options.parse_config_file(os.path.join(APP_ROOT, 'confs',
                                               'server_conf_dev.py'))
app = name_maker


class TestHandlerBase(AsyncHTTPTestCase):
    def setUp(self):
        super(TestHandlerBase, self).setUp()

    def get_app(self):
        return app

    def get_http_port(self):
        return options.port


class TestBucketHandler(TestHandlerBase):
    def test_get_req(self):
        response = self.fetch(
            '/',
            method='GET',
            follow_redirects=False)

        self.assertEqual(response.code, 200)
