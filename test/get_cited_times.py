# -*- coding:utf-8 -*-
"""
python3.7 win10 pycharm2017.2
2018.2.3
lenken liu
"""

import urllib.request
import re




#  url_01:存在直接结果，即有完全匹配的关键词，有唯一的结果。
#  url_02：存在多个结果，没有完全匹配的项。
url_01 = 'http://xueshu.baidu.com/s?wd=Evacuation%20planning%20with%20endogenous%20transportation%20network%20' \
         'degradations%3A%20a%20stochastic%20cell-based%20model%20and%20solution%20procedure'
url_02 = 'http://xueshu.baidu.com/s?wd=Macrotexture%20of%20Pavement%20Surface%20Treatments%20and%20Its%20Effect%20' \
         'on%20Bicycle%20Ride%20Quality'

request_01 = urllib.request.Request(url_01, headers=headers)
request_02 = urllib.request.Request(url_02, headers=headers)

response_01 = urllib.request.urlopen(request_01)
response_02 = urllib.request.urlopen(request_02)

codes_01 = response_01.read().decode('utf-8')
codes_02 = response_02.read().decode('utf-8')

content_pattern = re.compile('''{'button_tp':'sc_cited'}">.*?(\d+?).*?</a>''', re.S)
#  pattern解读：
#  一定以‘{'button_tp':'sc_cited'}">’开头，以'</a>'结尾；
#  在这两个之间，至少存在一个或存在多个数字：\d+。且这种数字的匹配不是贪心的，故加？并得到要获得的项：(\d+?)
#  在(\d+?)前后，可能存在多个（不确定数量的）任意的字符，用.*?代表。

result_01 = re.findall(content_pattern, codes_01)
result_02 = re.findall(content_pattern, codes_02)
#  注意：result是一个元素为字符的序列。所以要取他的0位，并格式化为数字。

result_01_int = int(result_01[0])
if len(result_02) > 1:
    result_int = []
    for i in range(len(result_02)):
        result_int.append(int(result_02[i]))
else:
    result_int = int(result_02[0])

"""为了处理零引用，整合如下：(三个result代表三种可能的搜索结果)"""
result = ['1', '1', '1', '5']  #  此情况下：一定有多种搜索结果，人工排查
# result = None  #  可能是唯一结果且引用次数为0，也可能有多个结果但他们的引用次数全是0
# result = ['5']  #  可能是唯一结果且引用次数为5，也可能有多个结果但他们的引用次数除一个为5以外其余全是0
if result:
    if len(result) > 1:
        result_int = []
        for i in range(len(result)):
            result_int.append(int(result[i]))
    else:
        result_int = int(result[0])
else:
    result_int = 0
print('引用次数：', result_int)

# ================   潜在漏洞：  ====================
# 对于一个没有完全匹配项的论文题目的结果，如果他的所有结果项的引用次数都是零，或者只有一篇有引用次数，
# 这个空结果或者唯一结果可能被程序误认为是唯一的正确结果。
# 解决潜在漏洞：distinguish_search_result.py
# ===================================================

# print('有单一结果：',  result_01_int)
# print('有多个结果：',  result_int)


"""
目的：
原来的匹配模式不完善。

问题一：
content_pattern = re.compile('''{'button_tp':'sc_cited'}">(.*?)</a>''', re.S)
在这个匹配模式下，结果形式为：
['\r\n                                    1\r\n    \r\n            ']
所以要优化pattern。

问题二：
有时候关键词没有完全匹配的项，所以打开的网页有多个结果，有多个应用量会被检索到，形式如：
['\n                                    2\r\n    \n            ', '\n                                    32\r\n    \n 
', '\n                                    2\r\n    \n            ', '\n                                    2\r\n    \n 
          ', '\n                                    150\r\n    \n            ', '\n                                    
          41\r\n    \n            ', '\n                                    5\r\n    \n            ', '\n              
                                10\r\n    \n            ', '\n                                    11\r\n    \n        
']
针对这个情况也需要改进。(这种可能只能人工识别了)

结果：（整合后的）
引用次数：[1, 1, 1, 5]
引用次数：0
引用次数：5

结论：
简单处理即可解决问题。

"""
