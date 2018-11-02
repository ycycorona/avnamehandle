from lib.excel_file_util import ExcelFileUtil
from lib.avmoo_search_video_info import  find_video_fullname
import pathlib
base_url = 'https://avmoo.net/cn/search/'


def get_new_name_excel(before_handle_excel_file_path, table_header_tuple):
    before_handle_list = ExcelFileUtil.read_list_form_excel_file(before_handle_excel_file_path)
    for video_item in before_handle_list:
        url = base_url + video_item['av_id']
        video_item['new_av_name'] = find_video_fullname(url)
        print(video_item)
    after_handle_excel_file_path = ExcelFileUtil.save_files_list(
        'av_name', before_handle_list, table_header_tuple, 'after', pathlib.PurePath(before_handle_excel_file_path).parent)


if __name__ == '__main__':
    table_header_tuple = ('av_id', 'file_name', 'new_av_name', 'path')
    handle_path = r'G:\\'  # 入口
    before_handle_excel_file_path = r'D:\code\personal\avnamehandle\enter\G---before-1540727409.xlsx'
    get_new_name_excel(before_handle_excel_file_path, table_header_tuple)
    pass
