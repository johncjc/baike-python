"""
Html输出器
"""
import openpyxl
import pandas as pd
import numpy as np

class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        """
        收集数据
        :param data:
        :return:
        """
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        """
        将收集结果输出成Html页面
        :return:
        """

        file_out = open('./output/output.txt', 'w',encoding='utf-8')
        for data in self.datas:

            # baike = data['summary']
            # baike2 = data['title']
            # print(baike, baike2)
            # DataSet = list(zip(baike, baike2))
            # juzhen = np.mat(DataSet)
            # df = pd.DataFrame(juzhen)
            # df.to_excel('r.xlsx')
            file_out.write('%s\t%s\t%s\t%s\n'%(data['if'],data['tag'],data['title'],data['summary']))
        file_out.close()