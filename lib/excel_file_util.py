# openpyxl==2.5.9
import openpyxl
import time  # 引入time模块
import pathlib


class ExcelFileUtil(object):
    def __init__(self):
        pass

    @staticmethod
    def read_list_form_excel_file(file_path) -> list:
        wb = openpyxl.load_workbook(file_path)
        ws = wb.active  # 默认取当前激活的sheet
        t_rows = tuple(ws.rows)  # generator 转 tuple
        list_1 = []
        dic_key_tuple = []

        # 取出表头
        for th in t_rows[0]:
            dic_key_tuple.append(th.value)
        dic_key_tuple = tuple(dic_key_tuple)

        # 取出表内容
        for i in range(1, len(t_rows)):
            dic_1 = {}
            for j in range(len(dic_key_tuple)):
                dic_1[dic_key_tuple[j]] = t_rows[i][j].value if t_rows[i][j] else ''
            list_1.append(dic_1)
        return list_1
        pass

    @classmethod
    def save_files_list(cls, base_xls_name, files_list, table_header_tuple=None, name_prefix='', output_path=''):
        """
        :keyword 持久化列表到xlsx文件
        :param base_xls_name: 基础文件名
        :param files_list: 要持久化的list
        :param table_header_tuple: 表头
        :param name_prefix: 文件后缀
        :param output_path: 输出路径
        :return:
        """
        # 新建文件
        workbook = openpyxl.Workbook()
        # 写入文件
        if not table_header_tuple:
            table_header_tuple = cls.get_th_from_list(files_list)
        sheet = workbook.active
        sheet.append(table_header_tuple)
        for file_obj in files_list:
            sheet.append([file_obj[th] if th in file_obj else '' for th in table_header_tuple])
        save_files_path = '%s-%s-%d.xlsx' % (base_xls_name, name_prefix, int(time.time()))
        workbook.save(output_path + save_files_path)  # 保存文件
        return output_path + save_files_path

    @staticmethod
    def get_th_from_list(list_1):
        list_res = []
        if not len(list_1):
            return tuple()
        for th in list_1[0]:
            list_res.append(th)
        return tuple(list_res)


if __name__ == '__main__':
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
    table_header_Tuple = ('av_id', 'file_name', 'path')
    path = r'D:\code\personal\avnamehandle\local_storage\G---before-1540727409.xlsx'
    print(pathlib.PurePath(path).parent)

    #res_1 = ExcelFileUtil.save_files_list('test', ExcelFileUtil.read_list_form_excel_file(path))
    pass
