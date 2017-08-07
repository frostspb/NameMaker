function valid_grid_param(err_msg) {
    var valid_flag = true;
    try {
        var h = Number(document.getElementById('row_count').value);
        var w = Number(document.getElementById('col_count').value);

        if ((h <= 0) || (w <= 0)) {
            valid_flag = false;
            alert(err_msg)
        }

    }
    catch (err) {
        valid_flag = false;
    }
    if (valid_flag) {

        document.getElementById('grid_param_f').submit();
    }

}


var rotateClockwise = function (matrix) {
    // reverse the rows
    //matrix = matrix.reverse();

    for (var i = 0; i < matrix.length; i++) {
        for (var j = 0; j < i; j++) {
            var temp = matrix[i][j];
            matrix[i][j] = matrix[j][i];
            matrix[j][i] = temp;
        }
    }
};


function collect_data_matrix(err_tmpl) {
    var res = [];
    var valid_flag = true;
    var f = document.getElementById("permut_tb");
    var rows_count = f.rows.length;
    for (var i = 0; i < rows_count; i++) {
        var res_row = [];
        var cell_count = f.rows[i].cells.length;

        for (var j = 0; j < cell_count; j++) {
            var v = f.rows[i].cells[j].getElementsByTagName('input')[0].value;
            if (v == '') {
                "{0}{1}".format("{1}", "{0}")

                var s2 = "My name: {0}, age: {1}!".f(i, j);
                alert(err_tmpl.f(i, j));
                valid_flag = false;
            }
            else {
                res_row.push(v)
            }

        }
        res.push(res_row)
    }

    if (valid_flag) {
        var newGrid = JSON.parse(JSON.stringify(res));
        document.getElementById('res_d').value = JSON.stringify(newGrid);
        document.getElementById('h_tbl').value = document.getElementById('row_count').value;
        document.getElementById('w_tbl').value = document.getElementById('col_count').value;
        document.getElementById('push_form').submit();
    }

}

function getCookie(name) {
    var matches = document.cookie.match(new RegExp(
        "(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
    ));
    return matches ? decodeURIComponent(matches[1]) : undefined;
}

function setCookie(name, value, options) {
    options = options || {};

    var expires = options.expires;

    if (typeof expires == "number" && expires) {
        var d = new Date();
        d.setTime(d.getTime() + expires * 1000);
        expires = options.expires = d;
    }
    if (expires && expires.toUTCString) {
        options.expires = expires.toUTCString();
    }

    value = encodeURIComponent(value);

    var updatedCookie = name + "=" + value;

    for (var propName in options) {
        updatedCookie += "; " + propName;
        var propValue = options[propName];
        if (propValue !== true) {
            updatedCookie += "=" + propValue;
        }
    }

    document.cookie = updatedCookie;
}


function switch_lang() {

    var cur_lang = getCookie('cur_lang');
    if (cur_lang == 'ru') {

        cur_lang = 'en'
    }
    else  if (cur_lang == 'en') {

        cur_lang = 'ru'
    }
    else {

        cur_lang = 'en'
    }

    setCookie('cur_lang', cur_lang);
    window.location.reload()
}






