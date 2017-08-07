# -*- coding: utf-8 -*-
import hashlib
from nmlib.base_grid_view import GridPage
from nmlib.base_tornado_lib.base_tor_handler import NMBaseHandler
import json
import itertools
import os
import xlsxwriter
from confs.app_config import MAX_GEN_RECORDS

from concurrent.futures import ThreadPoolExecutor
from tornado.concurrent import run_on_executor
from nmlib.handlers.permut_app.nm_utils import get_data_permut

import functools, itertools, operator
from confs.app_config import DEFAULT_RECORDS_COUNT, MAX_EXC_RECORDS

from nmlib.handlers.permut_app.nm_utils import get_fmt_count
from nmlib.handlers.permut_app.loc import loc_dict, WAITE_MSG, ERR_MSG



class PermutHandler(NMBaseHandler):
    def __init__(self, application, request, **kwargs):
        super().__init__(application, request, **kwargs)
        self.max_records = MAX_GEN_RECORDS
        self.count_combinations = 0
        self.count_step = DEFAULT_RECORDS_COUNT
        #self.user_l = 'ru'
        self.executor = ThreadPoolExecutor(max_workers=os.cpu_count())

    def get(self):
        str_matrix = self.get_argument('res_d', False)
        h = self.get_argument('h_tbl', False)
        w = self.get_argument('w_tbl', False)
        self.render('calc_timer.html', src_str=str_matrix, msg=loc_dict[self.user_l][WAITE_MSG], user_l=self.user_l,
                    h=h, w=w, err_msg=loc_dict[self.user_l][ERR_MSG],)

    def get_format_data(self, str_matrix):
        #TODO TRY
        matrix = json.loads(str_matrix)
        rotated = list(zip(*matrix[::1]))
        return rotated

    def get_permut_data(self, src_data, count=DEFAULT_RECORDS_COUNT):
        self.count_step = count
        return get_data_permut(src_data, self.count_step)

    @run_on_executor
    def export_to_xls(self, data_source):
        """
        В отдельном потоке читает файл
        :param path: путь до файла
        :return: содержимое файла
        """
        workbook = xlsxwriter.Workbook('static/names.xlsx')
        worksheet = workbook.add_worksheet()
        row = 0
        for r in data_source:
            col = 0
            for c in r:
                worksheet.write(row, col, c)
                col += 1
            row += 1
        workbook.close()

    def post(self):
        
        str_matrix = self.get_argument('res_d', False)
        to_excel = self.get_argument('to_excel', False)
        h = self.get_argument('h_tbl', False)
        w = self.get_argument('w_tbl', False)

        # hash_str = self.get_hash_str(str_matrix)
        self.fmt_data = self.get_format_data(str_matrix)
        len_t = functools.reduce(operator.mul, map(len, self.fmt_data), 1)

        self.count_combinations = len_t
        self.log_debug('len grid = %s' % self.count_combinations)
        if to_excel:
            count_r = MAX_EXC_RECORDS
        else:
            count_r = DEFAULT_RECORDS_COUNT
        permut_result = self.get_permut_data(self.fmt_data, count_r)

        self.log_debug('len grid = %s' % self.count_combinations)
        # permut_result=permut_result1
        displayed = self.count_step if self.count_step < self.count_combinations else self.count_combinations

        rndr_dict = {
            'arg': permut_result,
            'rec_count': self.count_combinations,
            'rec_count_fmt': get_fmt_count(self.count_combinations),
            'rec_show_count': get_fmt_count(displayed),
                     }
        if to_excel:
            self.export_to_xls(permut_result).result()
            self.write(self.static_url('names.xlsx'))
            self.finish()

        else:

            self.render('result_permut.html', rn_data=rndr_dict, loc=loc_dict[self.user_l], user_l=self.user_l,
                    str_matrix=str_matrix, h=h, w=w, err_msg=loc_dict[self.user_l][ERR_MSG],)



