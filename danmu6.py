#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 11:16:47 2018

@author: talin
propose giftdata and massage ,we need 7days data
save all audience giftinfo as a csv file
save all audience massage as a csv file
"""
import pandas as pd
import gc

# save a date giftmassage system_massage ID steamp
data1 = pd.read_table('message_info_data_2018-09-01.txt', sep="\t", header=None)
data2 = pd.read_table('message_info_data_2018-09-02.txt', sep="\t", header=None, error_bad_lines=False)
data3 = pd.read_table('message_info_data_2018-09-03.txt', sep="\t", header=None)
data4 = pd.read_table('message_info_data_2018-09-04.txt', sep="\t", header=None)
data5 = pd.read_table('message_info_data_2018-09-05.txt', sep="\t", header=None)
data6 = pd.read_table('message_info_data_2018-09-06.txt', sep="\t", header=None)

data = pd.concat([data1, data2, data3, data4, data5, data6], axis=0, join='outer')
# data_gift=data.drop(columns=[1,2,3,4,5,6,8,10,13],axis=1)
data_gift = pd.DataFrame(data={'stamp': data[0], 'date': data[12],
                               'msg': data[10]})
data_gift.to_csv('msg_6.txt', sep='\t')
gc.collect()




