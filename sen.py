#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 22:09:02 2019

@author: talin
"""

import pandas as pd
from snownlp import SnowNLP
import matplotlib.pyplot as plt
# import commonFunction as cf
import numpy as np
'''
# 处理数据成分钟时间加弹幕信息
data = pd.read_table('message_info_data_2018-09-02.txt', sep='\t', header=None, error_bad_lines=False)

time = pd.DataFrame(cf.spTime(data[1]),columns=['year','month','day','hour','minute','second'])
a = time['hour'].tolist
msg=pd.DataFrame({'msg':data[10],'minute':time.minute+time.hour*24})
'''

'''
#画出情感分布图
tag=data[10][:1000000]
tag.dropna(inplace=True)
tmp = []
for i in tag:
    tmp+=[(SnowNLP(i).sentiments/2)-0.5]

tmp.sort(reverse=False)
plt.bar(tmp,range(len(tmp)))
'''
data = pd.read_table('minute_msg_02.txt', sep="\t")

a = data.dropna()
group = a.groupby('minute')
minute = [x for x in group]

ress = []
for i in range(len(minute)):
    for x in minute[i][1]['msg']:
        res = []
        # res={i:[SnowNLP(x).sentiments]}
        res += [SnowNLP(x).sentiments]
        ress.append(res)


def wilson_score(pos, total, p_z=2.):
    """
    :param pos: 正例数
    :param total: 总数
    :param p_z: 正太分布的分位数
    :return: 威尔逊得分
    """
    pos_rat = pos * 1. / total * 1.  # 正例比率
    score = (pos_rat + (np.square(p_z) / (2. * total))
             - ((p_z / (2. * total)) * np.sqrt(4. * total * (1. - pos_rat) * pos_rat + np.square(p_z)))) / \
            (1. + np.square(p_z) / total)
    return score

