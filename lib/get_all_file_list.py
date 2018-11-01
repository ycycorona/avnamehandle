from pathlib import Path
from os import walk
files_count = 0
sub_dir_count = 0


def file_obj_gen(path, file_name):
    return {
        'path': path,
        'file_name': file_name
    }


def main(work_root_path_string):
    file_list = get_files(Path(work_root_path_string))
    if __name__ == '__main__':
        by_product()
    return file_list


def get_files(path):
    global files_count
    global sub_dir_count
    file_list = list()
    for root, dirs, files in walk(path):
        for file in files:
            files_count += 1
            file_list.append(file_obj_gen(root, file))
            # print(Path(root, file))
        for name in dirs:
            sub_dir_count += 1
            # print('dir %s' % PureWindowsPath(root, name).__str__())
    return file_list


def by_product():
    # 显示文件总数
    print('文件总数：%s' % files_count)
    # 显示子目录数
    print('子目录总数：%s' % sub_dir_count)


if __name__ == '__main__':
    main(r'E:\local note\工作')

