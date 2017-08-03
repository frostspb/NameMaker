# -*- coding: utf-8 -*-

from nmlib.base_grid_view import GridPage
from nmlib.base_tornado_lib.base_tor_handler import NMBaseHandler
import json
import itertools


class IndexPage(GridPage):

    def get(self):
        self.render('index.html', h=self.GRID_ROW, w=self.GRID_COL)

    def post(self):
        h = int(self.get_argument('row_count', self.GRID_ROW))
        w = int(self.get_argument('col_count', self.GRID_COL))
        self.render('data_input.html', grid=self.get_grid_list(h=h, w=w))


class PermutHandler(NMBaseHandler):

    def get_data_permut(self, src_data):
        try:
            matrix = json.loads(src_data)
            permut = list(itertools.product(*matrix))
            permut_result = [(''.join(i),) + i for i in permut]
        except Exception:
            self.log_exc('get_data_permut failed')
            permut_result = None
        return permut_result

    def post(self):
        str_matrix = self.get_argument('res_d')

        permut_result = self.get_data_permut(str_matrix)

        self.render('result_permut.html', arg=permut_result)


