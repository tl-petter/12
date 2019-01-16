import pandas as pd
import jieba.analyse
import commonFunction as cf
import jieba
import matplotlib.pyplot as plt

data=pd.read_table('msg_6.txt',sep='\t')

#tags=jieba.analyse.extract_tags(cf.dftostr(data['msg']))
#print("\n".join(tags))

tag_list = [list(jieba.cut(cf.dftostr(data['msg'])))]
plt.bar(range(len(tag_list),tag_list))