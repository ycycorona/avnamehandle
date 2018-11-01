from lib.excel_file_util import read_list_form_excel_file
from lib.avmoo_search_video_info import  find_video_fullname
from lib.save_files_list import save_files_list
base_url = 'https://avmoo.net/cn/search/'


def get_new_name_list(before_handle_excel_file_path, handle_path, table_header_tuple):
    before_handle_list = read_list_form_excel_file(before_handle_excel_file_path)
    for video_item in before_handle_list:
        url = base_url + video_item['av_id']
        video_item['new_av_name'] = find_video_fullname(url)
        print(video_item)
        pass
    after_handle_excel_file_path = save_files_list(handle_path, 'after', before_handle_list, table_header_tuple)
    pass


if __name__ == '__main__':
    table_header_tuple = ('av_id', 'file_name', 'new_av_name', 'path')
    handle_path = r'G:\\'  # 入口
    before_handle_excel_file_path = r'D:\code\personal\avnamehandle\enter\G---before-1540727409.xlsx'
    get_new_name_list(before_handle_excel_file_path, handle_path, table_header_tuple)
    pass
