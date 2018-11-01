from os import path
import re
import copy
from lib.video_type import video_type
AV_ID = 'av_id'
EXTENSION = 'extension'
pattern = r'(?<=[-_0-9])[a-zA-Z]{2,}-?\d{2,}|[a-zA-Z]{2,}-?\d{2,}'
pattern_obj = re.compile(pattern)


def file_name_filter(files_list):
    valid_file_list = list()
    for file_obj in files_list:
        extension = str.lower(path.splitext(file_obj['file_name'])[-1][1:])
        main_name = ''.join(path.splitext(file_obj['file_name'])[:-1])
        if extension in video_type:  # 判断扩展名
            re_result = pattern_obj.findall(main_name)  # 正则取出有效番号
            if re_result:
                valid_file_list.append(copy.deepcopy(file_obj))
                valid_file_list[-1][AV_ID] = re_result[-1]
                valid_file_list[-1][EXTENSION] = extension
    return valid_file_list


if __name__ == '__main__':
    file_name_filter([{
        'file_name': 'abp-123.avi',
        'path': 'E:\\local note\\工作'
    }])
