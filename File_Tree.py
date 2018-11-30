# -*- encoding: utf-8 -*-
import os

MID_CHAR = '├─'
LEAF_CHAR = '└─'
VERTICAL_CHAR = '│'

FILE = open('tree.txt', 'w')


def parse_file_tree(cur_path):
    depth = len(cur_path.split('/')) - 1
    item_num = len(os.listdir(cur_path))
    dirs = []
    files = []

    if depth == 0:
        FILE.writelines('.\n')
    for item in os.listdir(cur_path):
        if '.' in item:
            files.append(item)
        else:
            dirs.append(item)

    print(dirs)
    print(files)
    if len(dirs) == 0 and len(files) == 0:
        return
    if len(dirs) > 0:
        if len(files) == 0:
            for i in range(len(dirs)):
                if i == len(dirs) - 1:
                    FILE.writelines(VERTICAL_CHAR + '\t' * depth + LEAF_CHAR + dirs[i] + '\n')
                else:
                    FILE.writelines(VERTICAL_CHAR + '\t' * depth + MID_CHAR + dirs[i] + '\n')
                new_path = cur_path + '/' + dirs[i]
                # print(new_path)
                parse_file_tree(new_path)
        else:
            for i in range(len(dirs)):
                FILE.writelines(VERTICAL_CHAR + '\t' * depth + MID_CHAR + dirs[i] + '\n')
                new_path = cur_path + '/' + dirs[i]
                # print(new_path)
                parse_file_tree(new_path)

    if len(files) > 0:
        for i in range(len(files)):
            if i == len(files) - 1:
                FILE.writelines(VERTICAL_CHAR + '\t' * depth + LEAF_CHAR + files[i] + '\n')
            else:
                FILE.writelines(VERTICAL_CHAR + '\t' * depth + MID_CHAR + files[i] + '\n')


if __name__ == '__main__':
    parse_file_tree(os.curdir)
    FILE.close()
