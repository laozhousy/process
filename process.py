import pandas as pd
# 设置显示的最大列、宽等参数，消掉打印不完全中间的省略号
# pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 10240)#加了这一行那表格的一行就不会分段出现了
# pd.set_option('display.max_colwidth', 1000)
# pd.set_option('display.height', 1000)
#显示所有列
pd.set_option('display.max_columns', None)
#显示所有行
pd.set_option('display.max_rows', None)
#设置value的显示长度为100，默认为50
pd.set_option('max_colwidth',500)

pre=pd.read_csv("original_file/dev.tsv",sep='\t',usecols=[2,4])
print(pre)
pre.index = pre.index + 1
pre.to_csv('preprocessing_file/dev.tsv',sep='\t',index=1,header=1)

# pre=pd.read_csv("original_file/train.tsv",names=['tweet','emotion'])
# pre.index = pre.index + 1
# pre.to_csv('preprocessing_file/train.tsv',columns=['tweet','emotion'],index=1,header=1)

pre=pd.read_csv("preprocessing_file/dev.tsv",sep='\t')
pre.columns = ['id','text','label']
pre.to_csv('preprocessing_file/dev.tsv',sep='\t',columns=['id','text','label'],index=0,header=1)

