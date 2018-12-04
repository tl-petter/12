# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 15:01:02 2018
live_user_info_2018-09-01.txt
@author: Administrator
"""

import pandas as pd
import commonFunction as cf
import matplotlib.pyplot as plt
import jieba
import jieba.analyse
from wordcloud import WordCloud

data = pd.read_table('message_info_data_2018-09-01.txt',sep="\t",header = None)

# p is the data columns of online numbers 
#load data return datatrame has time feature and p feature
def loadData(p,data):
    #data = pd.read_table('live_user_info_2018-09-01.txt',sep="\t",header = None)
    
    dataStamp = pd.DataFrame(cf.spTime(data[1]),columns=['year','month','day','hour','minute','secound'])
    
    dataFinal = pd.concat([dataStamp,data[p]],axis=1)
    return dataFinal

#polt gift online number 24 hour
def poltnumber(p): 
    """
    :desc:
    :in
    """
    print('polt num+++')
    #polt data feature distribution user info data online number
    
    a = pd.DataFrame(loadData(p,data).groupby('hour')[p].sum().reset_index())
            
    plt.plot(a['hour'], a[p])
    
    
    plt.xlabel('hour')
    
    plt.ylabel('online number' )
    
    plt.title('gitf info online number  ' )
    #save dpi not too large
    fig = plt.figure(1, figsize=(8, 14), frameon=False, dpi=100)
    fig.add_axes([0, 0, 1, 1])
    plt.savefig('fig2.png',dpi=100)


poltnumber(7)

def poltword(p):
    #dftolist(data) is text list
    tags = jieba.analyse.extract_tags(cf.dftostr(data[p]),topK = 20)
    print("\n".join(tags))
    
    #words_ls = jieba.cut(cf.dftostr(data[p]), cut_all=True)
    #words_split1 = " ".join(words_ls)
    words_split2 = " ".join(tags)
    wc1 = WordCloud(
    width = 1980,
    height = 1680
                )
    wc1.font_path="msyh.ttf "
    wc2 = WordCloud(
    width=400,
    height=200,
    background_color="#ffffff",  # 设置背景颜色
    max_words=500,  # 词的最大数（默认为200）
    max_font_size=60,  # 最大字体尺寸
    min_font_size=10,  # 最小字体尺寸（默认为4）
    colormap='bone',  # string or matplotlib colormap, default="viridis"
    random_state=10,  # 设置有多少种随机生成状态，即有多少种配色方案
    font_path='simhei.ttf'
                        )

    #my_wordcloud1 = wc1.generate(words_split1)
    my_wordcloud2 = wc2.generate(words_split2)
    plt.imshow(my_wordcloud2)
#poltword(8)
