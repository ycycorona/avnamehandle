import openpyxl
import time  # 引入time模块
import re


def save_files_list(base_xls_name, name_prefix, files_list, table_header_tuple):
    # 新建文件
    workbook = openpyxl.Workbook()
    # 写入文件
    sheet = workbook.active
    sheet.append(table_header_tuple)
    for file_obj in files_list:
        sheet.append([file_obj[th] if th in file_obj else '' for th in table_header_tuple])
    save_files_path = re.sub(r':\\|\\|:', '-', base_xls_name) + '-' + name_prefix + '-' + str(int(time.time())) + '.xlsx'
    workbook.save(save_files_path)  # 保存文件
    return save_files_path


if __name__ == '__main__':
    table_header_tuple = ('av_id', 'file_name', 'path')
    fl = [{
        'path': 'F:\\Downloads',
        'file_name': 'MIGD-630 中出しブラック企業 川村まや.mkv',
        'av_id': 'MIGD-630',
        'extension': 'mkv'
    }, {
        'path': 'F:\\Downloads',
        'file_name': 'MXGS-566 肉食系エログラマラス 水沢のの.mp4',
        'av_id': 'MXGS-566',
        'extension': 'mp4'
    }, {
        'path': 'F:\\Downloads',
        'file_name': 'NBD-082 お嬢様残酷調教倶楽部 黒木いくみ.mp4',

    }]
    save_files_list(r'D:\Code\py\avnamehandle', fl, table_header_tuple)
