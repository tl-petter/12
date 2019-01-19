import pandas as pd
import numpy as np
import jieba.analyse
import commonFunction as cf
import jieba
import matplotlib.pyplot as plt

data=pd.read_table('msg_6.txt',sep='\t')

tags=list(jieba.analyse.extract_tags(cf.dftostr(data['msg']),topK=100))

#print("\n".join(tags))

#tag_list = jieba.cut(cf.dftostr(data['msg']))
#print(", ".join(tag_list))


words_df = pd.DataFrame({'segment': tags})

# 分组
books_stat = words_df.groupby(by=['segment'])['segment'].agg({"count": np.size})
# 排序
books_stat = books_stat.reset_index().sort_values(by=["count"], ascending=False)

le = ['快乐','安心','乐','开心','高兴','大笑','笑','好欢','呵呵','好吃']
hao = ['赞扬','喜爱','感动','好看']
nv = ['怒','愤怒','发火','生气','发脾气','怒吼','得罪','吊炸','气炸','吼吼']
chou = ['悲伤','失望','愧疚','郁闷','尴尬','无奈','难过','自责','莫名','嘲讽']
jing = ['惊','哇塞','压惊','奇怪','看起来']
wu = ['厌恶','贬责','烦','讽刺','讨厌','恶心','嫌弃','有毒','诅咒','装逼','恶意','得罪','打架','不能']
ju = ['慌','恐惧','怕','担心','吓人','叹气','闭嘴','不想']

# 对情感词典匹配
le_num = [x[1] for x in books_stat.values if (x[0] in le)]
hao_num = [x[1] for x in books_stat.values if (x[0] in hao)]
nv_num = [x[1] for x in books_stat.values if (x[0] in nv)]
chou_num = [x[1] for x in books_stat.values if (x[0] in chou)]
jing_num = [x[1] for x in books_stat.values if (x[0] in jing)]
wu_num = [x[1] for x in books_stat.values if (x[0] in wu)]
ju_num = [x[1] for x in books_stat.values if (x[0] in ju)]

# 统计每种情感词出现次数
sum_le = sum(le_num)
print(sum_le)
sum_hao = sum(hao_num)
print(sum_hao)
sum_nv = sum(nv_num)
print(sum_nv)
sum_chou = sum(chou_num)
print(sum_chou)
sum_jing = sum(jing_num)
print(sum_jing)
sum_wu = sum(wu_num)
print(sum_wu)
sum_ju = sum(ju_num)
print(sum_ju)

#将7种情感统计合并成矩阵
classes= ['乐','好','怒','恶','惊','愁','惧']
count=[sum_le,sum_hao,sum_nv,sum_wu,sum_jing,sum_chou,sum_ju]
data = {"type":classes,
            "count":count}
df =pd.DataFrame(data,index= range(7),columns=['type','count'])
    #绘图
plt.rcParams['font.sans-serif'] = [u'SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.plot(classes, count,marker='o')
plt.xlabel('情感类别')
plt.ylabel('数量')
plt.title('折线图')
plt.savefig("情感词频图.jpg")
plt.show()