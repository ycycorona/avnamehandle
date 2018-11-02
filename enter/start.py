from enter.get_old_files_name_list import get_old_file_name_excel
from enter.get_new_file_name_list import get_new_name_excel

table_header_tuple = ('av_id', 'file_name', 'path')
handle_path = r'G:\\'  # 入口
rootPath = r'D:\Code\py\avnamehandle-git\\'



before_xls_path = get_old_file_name_excel(handle_path, table_header_tuple, rootPath)
#after_xls_path = get_new_name_excel(before_xls_path, table_header_tuple)
pass
