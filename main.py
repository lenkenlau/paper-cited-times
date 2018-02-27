# -*- coding:utf-8 -*-
"""
python3.7 win10 pycharm2017.2
2018.2.3
lenken lau
"""

import xlrd
from xlutils.copy import copy
import urllib.request
import urllib.error
import urllib.parse
import re

class Cited_Times:
    def __init__(self):
        self.user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
        self.headers = {'User-Agent': self.user_agent}
        self.enable = False

    def read_excel(self):
        excelfile = xlrd.open_workbook(r'C:\Python\Project\cited_times\2015papers.xls')
        sheet = excelfile.sheet_by_index(0)
        nrows = sheet.nrows
        paper_name = []
        for i in range(nrows):
            cell = sheet.cell(i, 0).value
            paper_name.append(urllib.parse.quote(cell))
        return [nrows, paper_name]

    def write_excel(self, nrows, cited_times):
        old_excelfile = xlrd.open_workbook(r'C:\Python\Project\cited_times\2015papers.xls')
        new_excelfile = copy(old_excelfile)
        new_sheet = new_excelfile.get_sheet(0)

        for i in range(1, nrows):
            new_sheet.write(i, 2, cited_times[i-1])
        print('finish write')
        new_excelfile.save('2015papers.xls')

    def get_Page(self, keyword):
        try:
            url = 'http://xueshu.baidu.com/s?wd=' + str(keyword)
            print(url)
            request = urllib.request.Request(url, headers=self.headers)
            response = urllib.request.urlopen(request)
            pageCode = response.read().decode('utf-8')
            return pageCode
        except urllib.error.HTTPError as e:
            if hasattr(e, "reason"):
                print("error", e.reason)
                return None

    def get_resultsnum(self, pageCode):
        resultsNum_pattern = re.compile('''curResultNum:"(\d+?)",''', re.S)  # resultsNum_pattern：结果数的正则表达模板
        resultsNum = re.findall(resultsNum_pattern, pageCode)  # resultsNum：结果数（一个字符串元素的序列）
        resultsNum_int = int(resultsNum[0])  # resultsNum_int：转resultsNum为数字
        return resultsNum_int

    def get_citedtimes(self, pageCode, resultsNum):
        content_pattern = re.compile('''{'button_tp':'sc_cited'}">.*?(\d+?).*?</a>''', re.S)  # result_pattern：引用数的正则表达模板
        result = re.findall(content_pattern, pageCode)  # result：引用数量（一个字符串元素的序列）

        if resultsNum == 1:
            # 因为结果数为1，故可以直接得到引用数
            if result:
                result_int = int(result[0])
            else:
                result_int = 0
        else:
            # 结果数大于1，没有准确结果
            result_int = 'No Accurate Answer'
        return result_int

    def start(self):
        # 调用read_excel()获得表格的行数（文章数）：nrows，以及文章题目序列：paper_names
        res_of_readexcel = self.read_excel()
        nrows = res_of_readexcel[0]
        paper_names = res_of_readexcel[1]

        # 新建一个序列cited_times，用来存放获得的引用数
        cited_times = []

        # 对paper_names内的所有文章进行检索，结果保存在cited_times中
        for i in range(1, nrows):
            # 获得网页代码：
            pageCode = self.get_Page(paper_names[i])
            # 获得检索得到的结果数量
            resultNum = self.get_resultsnum(pageCode)
            # 获得引用数量
            result = self.get_citedtimes(pageCode, resultNum)
            print('No.', i, ' times:', result)
            # 记录引用数量
            cited_times.append(result)

        # 写入到excel中去
        self.write_excel(nrows, cited_times)

Cited_Times().start()