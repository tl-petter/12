# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 15:36:20 2018
common function 
@author: Administrator
"""
import re
import time
#import pandas as pd
def timeStamp(timeNum):
    timeStamp = float(timeNum/1000)
    timeArray = time.localtime(timeStamp)
    otherStyleTime= time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return otherStyleTime



def spTime(data):
    tmp = []
    for i in data:
        pattern = re.compile(r'\d+')
        tmp.append(pattern.findall(timeStamp(i)))
    return tmp

def dftostr(dataframe):
    datatext = dataframe.fillna('')
    tmp = ''
    dataset = datatext.values
    for text in dataset:
        tmp += text
    return tmp
    