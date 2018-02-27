# -*- coding:utf-8 -*-
"""
python3.7 win10 pycharm2017.2
2018.2.3
lenken liu
"""

string = 'Evacuation planning with endogenous transportation network degradations: a stochastic cell-based model and solution procedure.'
new_string = string.replace(' ', '+')
print(new_string)


"""
目的：
在字符串中将所有空格替换为加号。

结果：
Evacuation+planning+with+endogenous+transportation+network+degradations:+a+stochastic+cell-based+model+and+solution+procedure.
完成替换

结论：
字符串有自带的replace功能，不用re模块。
且，python3中自带re模块。
"""

"""
改进
2018.2.3
"""
string = 'Evacuation planning with endogenous transportation network degradations: a stochastic cell-based model and solution procedure.'
new_string = string.replace(' ', '%2B')
print(new_string)

"""
改进结果：
原本是先用+替换空格再转码，这个时候+会转为%2B，在合成Url以后会使部分单字母失效，如'A'等。
后改为直接转码，不对空格做处理能直接解决问题，所以这个改进无用。
转空格为：%20。
"""