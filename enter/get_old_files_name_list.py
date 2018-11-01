from lib.get_all_file_list import main as get_all_file_list
from lib.filename_filter import file_name_filter
from lib.save_files_list import save_files_list


def get_old_file_name_excel(handle_path, table_header_tuple):
    filtered_files_list = file_name_filter(get_all_file_list(handle_path))
    before_handle_excel_file_path = save_files_list(handle_path, 'before', filtered_files_list, table_header_tuple)  # 保存为excel文件
    return before_handle_excel_file_path


if __name__ == '__main__':
    table_header_tuple = ('av_id', 'file_name', 'path')
    handle_path = r'G:\\'  # 入口
    get_old_file_name_excel(handle_path)

    pass
