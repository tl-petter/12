#coding=utf-8
'''
gift message feature count
find one days differedt our distrubtion of send gift number

2018_12_3 count audience send gift number use gift_info_data_2018-09-01.txt data
'''
import pandas as pd
import matplotlib.pyplot as plt

import commonFunction as cf
# data columms name or index
p = 5

data=pd.read_table('gift_info_data_2018-09-02.txt',sep="\t",header = None)
print('finish')
'''
def timeStamp(timeNum):
    timeStamp = float(timeNum/1000)
    timeArray = time.localtime(timeStamp)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return (otherStyleTime)



def spTime(data):
    tmp = []
    for i in data:
        pattern = re.compile(r'\d+')
        tmp.append(pattern.findall(timeStamp(i)))
    return tmp
'''

#use time feature 
#dataStamp = pd.DataFrame(cf.spTime(data[1]),columns=['year','month','day','hour','minute','secound'])

#dataFinal = pd.concat([dataStamp,data[p],data[5]],axis=1)
#polt data feature distribution

a = pd.DataFrame(data.groupby([6])[p].count()).reset_index()

fig = plt.figure()

ax = fig.add_subplot(1, 1 , 1)

plt.plot(a[6], a[p])


plt.xlabel('ID')

plt.ylabel('gift number' )

plt.title('distribution  ' )