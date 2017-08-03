# -*- coding: utf-8 -*-

from nmlib.base_tornado_lib.base_tor_handler import NMBaseHandler






class GridPage(NMBaseHandler):
    GRID_ROW = 3
    GRID_COL = 3
    NAME_CELL_TMPL = 'r%sc%s'
    NAME_ROW_TMPL = 'R%s'

    def __init__(self, application, request, **kwargs):
        super().__init__(application, request, **kwargs)
        self.grid_row_count = self.GRID_ROW
        self.grid_col_count = self.GRID_COL

    def get_grid_list(self, h=GRID_ROW, w=GRID_COL):
        res = [[{'row': self.NAME_ROW_TMPL % y,  'cell': self.NAME_CELL_TMPL % (y, i)} for i in range(w)] for y in range(h)]
        return res

