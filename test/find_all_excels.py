# -*- coding:utf-8 -*-
"""
python3.7 win10 pycharm2017.2
2018.2.3
lenken liu
"""

import os

L = []
# 路径
path = 'C:\Python\Project\cited_times\data'

for root, dirs, files in os.walk(path):
    # print(root)  # 打印当前目录路径
    # print(dirs)  # 打印当前路径下所有子目录（即子文件夹）
    # print(files)  # 打印当前路径下所有非目录子文件（即所有文件名）
    for file in files:
        # 其中os.path.splitext()函数将路径拆分为文件名 + 扩展名
        # 取出所有扩展名为xls或xlsx的文件名，放在L中
        if os.path.splitext(file)[1] == '.xls' or os.path.splitext(file)[1] == '.xlsx':
            L.append(os.path.join(file))
print(L)

"""
目的：
获取一个指定文件夹内所有扩展名为xls或xlsx的文件名

结果：
['2013paper.xlsx', '2014paper.xls', '2015paper.xls']

结论：
参考：https://www.cnblogs.com/strongYaYa/p/7200357.html

"""