import itertools
from string import ascii_lowercase
from confs.app_config import DEFAULT_GRID_W
from confs.app_config import MAX_GEN_RECORDS

import locale


def get_fmt_count(count_val):
    try:
        locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
        res = locale.format('%d', count_val, grouping=True)
    except Exception:
        res = count_val
    return res


def iter_all_strings():
    size = 1
    while True:
        for s in itertools.product(ascii_lowercase, repeat=size):
            yield "".join(s)
        size += 1


def get_debug_colname_vals(cols=DEFAULT_GRID_W):
    try:
        vals_iter = iter_all_strings()
        res = list(itertools.islice(vals_iter, cols))
    except Exception:
        res = []
    return res


def clear_none_val(matrix):
    return [x for x in matrix if x[0] is not None]


def is_empty(x):
    return '' not in x and '--' not in x


def filter_empty(val):
    return filter(is_empty, [list((''.join(x),) + x) for x in val])


def get_permut_result(src_data, count=MAX_GEN_RECORDS):
    count = count if isinstance(count, int) else MAX_GEN_RECORDS
    count = count if count <= MAX_GEN_RECORDS else MAX_GEN_RECORDS
    try:
        matrix = clear_none_val(src_data)
        permut_iter = itertools.product(*matrix)
        permut_result = (itertools.islice(filter_empty(permut_iter), count))
    except Exception:
        permut_result = []
    return permut_result
