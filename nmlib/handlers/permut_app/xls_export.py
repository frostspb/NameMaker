# -*- coding: utf-8 -*-



import os
import xlsxwriter
import time
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
from tornado.concurrent import run_on_executor
from nmlib.base_grid_view import GridPage

class XlsPage(GridPage):
    def __init__(self, application, request, **kwargs):

        super().__init__(application, request, **kwargs)
        self.executor = ThreadPoolExecutor(max_workers=os.cpu_count())
        self.fname_tmp = 'names_%s.xlsx'

    @run_on_executor
    def export_to_xls(self, data_source):
        """
        В отдельном потоке читает файл
        :param path: путь до файла
        :return: содержимое файла
        """
        t = int(time.mktime(datetime.now().timetuple()))
        fname = self.fname_tmp % str(t)
        workbook = xlsxwriter.Workbook('static/' + fname)
        worksheet = workbook.add_worksheet()
        row = 0
        for r in data_source:
            col = 0
            for c in r:
                worksheet.write(row, col, c)
                col += 1
            row += 1
        workbook.close()

    def get(self):
        self.render('index.html', h=self.grid_row_count, w=self.grid_col_count)

    def post(self):

        try:
            h = int(self.get_argument('row_count', self.grid_row_count))
            w = int(self.get_argument('col_count', self.grid_col_count))
            input_grid = self.get_grid_list(rows=h, cols=w)
        except:
            input_grid =[]
            self.log_exc('init grid fail')

        self.render('index.html', grid=input_grid)

