# -*- coding:utf-8 -*-
"""
python3.7 win10 pycharm2017.2
2018.2.3
lenken liu
"""

import urllib.parse

data1 = '乌贼'
data2 = 'dogs'

new_data1 = urllib.parse.quote(data1)
new_data2 = urllib.parse.quote(data2)

print('乌贼: ', new_data1)
print('dogs: ', new_data2)

"""
目的：
当处理含有中文的url时，会报错，提示：
UnicodeEncodeError: 'ascii' codec can't encode characters in position 12-28: ordinal not in range(128)
所以要对中文进行转码处理，即，转化成地址编码。形如：‘%E4%B9%8C%E8%B4%BC’

结果：
乌贼:  %E4%B9%8C%E8%B4%BC
dogs:  dogs

结论：
中文会被转换，但英文不受影响。
另：百度的编码是gbk，其他的一般网站比如google是utf8。
参考：http://www.jb51.net/article/86560.htm
"""

"""测试replace_space的改进（2018.2.3）"""
url = 'Evacuation%2Bplanning%2Bwith%2Bendogenous%2Btransportation%2Bnetwork%2Bdegradations:%2Ba%2Bstochastic%2Bcell-based%2Bmodel%2Band%2Bsolution%2Bprocedure.'
print(urllib.parse.quote(url))

"""结果：
Evacuation%252Bplanning%252Bwith%252Bendogenous%252Btransportation%252Bnetwork%252Bdegradations%3A%252Ba%252Bstochastic%252Bcell-based%252Bmodel%252Band%252Bsolution%252Bprocedure.
不行，代替空格的%2B会被改变。试着先转编码再处理空格。(中文没有空格，只有纯英文标题有空格)
操作后发现不用那么麻烦：“先转编码再处理空格”
直接转码就能解决问题
"""
