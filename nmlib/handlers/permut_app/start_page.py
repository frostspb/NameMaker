# -*- coding: utf-8 -*-
from nmlib.base_grid_view import GridPage


from nmlib.handlers.permut_app.loc import loc_dict, ERR_MSG,  ERR_D_MSG


class StartPage(GridPage):
    def __init__(self, application, request, **kwargs):
        super().__init__(application, request, **kwargs)
        #self.user_l = 'ru'

    def get(self):
        input_grid = self.get_grid_list()
        self.render('index.html', h=self.grid_row_count, w=self.grid_col_count, loc=loc_dict[self.user_l],
                    user_l=self.user_l, err_msg=loc_dict[self.user_l][ERR_MSG],
                    err_d_msg=loc_dict[self.user_l][ERR_D_MSG],
                    grid=input_grid)

    def post(self):

        try:
            h = int(self.get_argument('row_count', self.grid_row_count))
            w = int(self.get_argument('col_count', self.grid_col_count))
            input_grid = self.get_grid_list(rows=h, cols=w)
        except:
            input_grid =[]
            self.log_exc('init grid fail')

        self.render('index.html', h=self.grid_row_count, w=self.grid_col_count,
                    grid=input_grid, loc=loc_dict[self.user_l], user_l=self.user_l,
                    err_msg=loc_dict[self.user_l][ERR_MSG],err_d_msg=loc_dict[self.user_l][ERR_D_MSG],)

