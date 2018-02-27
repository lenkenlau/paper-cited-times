import urllib.request

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
headers = {'User-Agent': user_agent}

# 正常解码的地址：url0
url0 = 'http://xueshu.baidu.com/s?wd=Evacuation%20planning%20with%20endogenous%20transportation%20network%20degradations%3A%20a%20stochastic%20cell-based%20model%20and%20solution%20procedure'
# 出问题的地址：url
url = 'http://xueshu.baidu.com/s?wd=%E9%AB%98%E9%80%9F%E5%85%AC%E8%B7%AF%E5%B9%B3%E7%9B%B4%E8%B7%AF%E6%AE%B5%E9%9B%BE%E9%9C%BE%E5%A4%A9%E6%B0%94%E4%B8%8B%E7%9A%84IDM%E8%B7%9F%E9%A9%B0%E6%A8%A1%E5%9E%8B%E5%88%86%E6%9E%90'
request = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(request)
codes = response.read().decode('utf-8')  #,"ignore"

print(codes)

"""
目的：
解决问题，即在个别网页加载时报错：
UnicodeDecodeError: ‘utf8’ codec can’t decode byte 0xb0 in
'utf8'编解码器无法解码字节0xb0

结果：
未解决

结论：
"""
