# -*- coding:utf-8 -*-
"""
python3.7 win10 pycharm2017.2
2018.2.3
lenken liu
"""

import urllib.request
import re

#  使用代理
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
headers = {'User-Agent': user_agent}

url = ['http://xueshu.baidu.com/s?wd=Evacuation%20planning%20with%20endogenous%20transportation%20network'
       '%20degradations%3A%20a%20stochastic%20cell-based%20model%20and%20solution%20procedure',
       'http://xueshu.baidu.com/s?wd=Macrotexture%20of%20Pavement%20Surface%20Treatments%20and%20'
       'Its%20Effect%20on%20Bicycle%20Ride%20Quality']

for i in range(2):
    # 使用代理
    request = urllib.request.Request(url[i], headers=headers)
    response = urllib.request.urlopen(request)

    # 网页代码
    codes = response.read().decode('utf-8')

    # 确定得到了几个搜索结果
    resultsnum_pattern = re.compile('''curResultNum:"(\d+?)",''', re.S)  # resultsnum_pattern：结果数的正则表达模板
    resultsnum = re.findall(resultsnum_pattern, codes)  # resultsnum：结果数（一个字符串元素的序列）
    resultsnum_int = int(resultsnum[0])  # resultsnum_int：转resultsnum为数字

    # 获得引用数量
    result_pattern = re.compile('''{'button_tp':'sc_cited'}">.*?(\d+?).*?</a>''', re.S)  # result_pattern：引用数量的正则表达模板
    result = re.findall(result_pattern, codes)  # result：引用数量（一个字符串元素的序列）

    if resultsnum_int == 1:
        # 结果数为1，可以直接得到引用数
        if result:
            result_int = int(result[0])
        else:
            result_int = 0
    else:
        # 结果数大于1，没有准确结果
        result_int = 'No Accurate Answer'

    print(result_int)
