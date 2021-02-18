# 批量修改文件名
# 批量修改图片文件名
import os
import re
import time
import locale
import datetime
import sys
import shutil
import uuid


def mk_dirs(path):
    path = path.strip()
    path = path.rstrip("\\")  # 去除尾部 \ 符号
    is_exists = os.path.exists(path)
    if not is_exists:
        os.makedirs(path)  # 创建目录
        print(path + ' 创建成功')
        return True
    else:
        print(path + ' 目录已存在')
        return False


def timestamp_to_time_ym(timestamp):
    # print(timestamp)
    locale.setlocale(locale.LC_CTYPE, 'chinese')
    time_struct = time.localtime(timestamp)
    return time.strftime('%Y年%m月', time_struct)


def timestamp_to_time(timestamp):
    # print(timestamp)
    locale.setlocale(locale.LC_CTYPE, 'chinese')
    time_struct = time.localtime(timestamp)
    return time.strftime('%Y年%m月%d日%H%M%S', time_struct)


def get_file_create_time(filepath):
    # filePath = str(filePath)
    t = os.path.getctime(filepath)
    # print(t);
    return timestamp_to_time(t)


def get_file_create_time_ym(filepath):
    # filePath = str(filePath)
    t = os.path.getctime(filepath)
    # print(t);
    return timestamp_to_time_ym(t)


def get_obj_id():
    uid = str(uuid.uuid4())
    result = ''.join(uid.split('-'))
    return result[0:11]


def rename_all():
    filepath = r"C:\Users\Rex\Videos\王乙诺" #需要整理的文件目录
    file_list = os.listdir(filepath)  # 待修改文件夹
    # print("修改前："+str(fileList))		#输出文件夹中包含的文件
    current_path = os.getcwd()  # 得到进程当前工作目录
    os.chdir(filepath)  # 将当前工作目录修改为待修改文件夹的位置
    for fileName in file_list:  # 遍历文件夹中所有文件
        pat = ".+\\.(mp4)"  # 匹配文件名正则表达式
        pattern = re.findall(pat, fileName)  # 进行匹配
        print(pattern)
        if len(pattern) == 0:
            continue
        ym = get_file_create_time_ym(str(filepath + "\\" + fileName))
        print(ym)
        mk_dirs(str(filepath + "\\" + ym))
        basename = os.path.basename(str(filepath + "\\" + fileName))
        print("basename : " + basename)
        dirname = os.path.dirname(str(filepath + "\\" + fileName))
        print("dirname : " + dirname)
        new_name = (get_file_create_time(str(filepath + "\\" + fileName))) + "_" + get_obj_id() + '.' + pattern[0]
        os.rename(fileName, new_name)
        shutil.move(str(filepath + "\\" + new_name), str(filepath + "\\" + ym))
        # print("文件路径："+ filepath + "\\" + fileName)
        # print("文件创建时间："+ get_FileCreateTime(filepath + "\\" + fileName))
    print("---------------------------------------------------")
    os.chdir(current_path)  # 改回程序运行前的工作目录
    sys.stdin.flush()  # 刷新

    # print("修改后："+str(os.listdir(r"C:\Users\Rex\Videos\王乙诺")))		#输出修改后文件夹中包含的文件


rename_all()
