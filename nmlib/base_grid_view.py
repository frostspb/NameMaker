# -*- coding: utf-8 -*-

from nmlib.base_tornado_lib.base_tor_handler import NMBaseHandler
from confs.app_config import MAX_GRID_H, MAX_GRID_W
from confs.app_config import DEFAULT_GRID_H, DEFAULT_GRID_W
from nmlib.handlers.permut_app.nm_utils import get_debug_colname_vals


NAME_CELL_TMPL = 'r%sc%s'
NAME_ROW_TMPL = 'R%s'


class GridPage(NMBaseHandler):

    def __init__(self, application, request, **kwargs):
        super().__init__(application, request, **kwargs)
        self.grid_row_count = DEFAULT_GRID_H
        self.grid_col_count = DEFAULT_GRID_W
        self.cell_name_tmpl = NAME_CELL_TMPL
        self.row_name_tmpl = NAME_ROW_TMPL

    def get_cell_dict(self, col, row):

        x = self.get_col_names_list()

        c = x[col]

        cell_val = ''.join((c, str(row))) if self.nm_debug else ''
        return {
            'row': self.row_name_tmpl % row,
            'cell': self.cell_name_tmpl % (row, col),
            'value': cell_val
        }

    def get_grid_list(self, rows=DEFAULT_GRID_H, cols=DEFAULT_GRID_W):
        count_rows = rows if 0 < rows <= MAX_GRID_H else MAX_GRID_H
        count_cols = cols if 0 < cols <= MAX_GRID_W else MAX_GRID_W
        self.grid_row_count = count_rows
        self.grid_col_count = count_cols
        cols_iter = range(count_cols)
        rows_iter = range(count_rows)

        res = [[self.get_cell_dict(i, y) for i in cols_iter] for y in rows_iter]
        return res

    def get_col_names_list(self):
        return get_debug_colname_vals(self.grid_col_count)



