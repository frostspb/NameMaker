# -*- coding: utf-8 -*-
from nmlib.base_grid_view import GridPage


ERR_MSG = 'err_msg'
INPUT_PAR = 'input_par'
COL_COUNT = 'col_count'
ROW_COUNT = 'row_count'
REC_COUNT = 'rec_count'
NEXT_BTN = 'next'

GEN_BTN = 'gen_btn'
P_TITLE = 'p_tilte'
ERR_D_MSG = 'err_d_msg'


loc_dict = {
    'ru': {
        ERR_MSG: 'Проверьте данные',
        INPUT_PAR: 'Введите параметры',
        COL_COUNT: 'Кол-во  столбцов',
        ROW_COUNT: 'Кол-во  строк',
        REC_COUNT: 'Кол-во записей',
        NEXT_BTN: 'Далее',
        GEN_BTN: 'Генерируем!',
        P_TITLE: 'Введите данные',
        ERR_D_MSG: 'ячейка по адресу Строка {0} Столбец {1} не заполнена',
    },

    'en': {
        ERR_MSG: 'Check parameters!',
        INPUT_PAR: 'Enter the parameters',
        COL_COUNT: 'Rows count',
        ROW_COUNT: 'Cols count',
        REC_COUNT: 'Records count',
        NEXT_BTN: 'Next',
        GEN_BTN: 'Generate',
        P_TITLE: 'Input data',
        ERR_D_MSG: 'Cell at String {0} Column {1} is not filled',
    },


}


class StartPage(GridPage):
    def __init__(self, application, request, **kwargs):
        super().__init__(application, request, **kwargs)
        #self.user_l = 'ru'

    def get(self):
        input_grid = self.get_grid_list()
        self.render('index.html', h=self.grid_row_count, w=self.grid_col_count, loc=loc_dict[self.user_l],
                    user_l=self.user_l, err_msg=loc_dict[self.user_l][ERR_MSG], grid=input_grid)

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
                    err_msg=loc_dict[self.user_l][ERR_MSG])

