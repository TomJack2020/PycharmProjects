
import pandas as pd
from warnings import filterwarnings
filterwarnings('ignore')



# 读取导出数据
df_export = pd.read_csv('./中台模板/手动刊登小平台sku导出-2023-05-18-11-27-33-谌桥W00242.csv', encoding='ANSI')
print(df_export)


# 读取刊登sku数据表
df_kd = pd.read_excel('刊登SKU.xlsx')
print(df_kd)



# ['货号*', '价格，USD*', '增值税，%*', '商业类型*',
#                '毛重，克*', '包装宽度，毫米*', '包装高度， 毫米*', '包装长度，毫米*', '主照片的链接*',
#                '部件号（制造商的货号）*', '品牌*', '类型*', '型号名称*']

# 数据匹配
m1 = pd.merge(df_export, df_kd, on=['SKU'], how='left')
print(m1.columns)


cut_columns = ['SKU', '最新采购成本', '重量', '产品长', '产品宽', '产品高']
res = m1[cut_columns]
res.columns = ['货号*', '价格，USD*', '毛重，克*', '包装长度，毫米*', '包装宽度，毫米*', '包装高度， 毫米*']
print(res)
res.to_excel('res.xlsx', engine='xlsxwriter', index=False)
