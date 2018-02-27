# -*- coding:utf-8 -*-
"""
python3.7 win10 pycharm2017.2
2018.2.3
lenken liu
"""

import urllib.request

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
headers = {'User-Agent': user_agent}


url = 'http://xueshu.baidu.com/s?wd=Evacuation%20planning%20with%20endogenous%20transportation%20network%20degradations:%20a%20stochastic%20cell-based%20model%20and%20solution%20procedure.'
url02 = 'http://xueshu.baidu.com/s?wd=Evacuation+planning+with+endogenous+transportation+network+degradations%3A+a+stochastic+cell-based+model+and+solution+procedure.'
request = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(request)
codes = response.read().decode('utf-8')

print(codes)

"""
目的：
在运行时，网页解析出错。错误提示：
http.client.RemoteDisconnected: Remote end closed connection without response
应该是无反应，经分析应该是url格式问题。

结果：
无论是url还是url02都能返回正确的code
说明从excel中代入的数据组成的url有问题。

结论：
在程序中print出合成的url如下：
http://xueshu.baidu.com/s?wd=Evacuation planning with endogenous transportation network degradations: a stochastic cell-based model and solution procedure.
应该是解析时以空格为结束标记，所以将“http://xueshu.baidu.com/s?wd=Evacuation”视作为了地址，后面的所有内容可能导致了错误。
解决：把所有的空格批量换成加号“+”。
"""
