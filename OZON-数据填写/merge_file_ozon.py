import pandas as pd
import numpy as np
import xlwings as xw

app = xw.App(visible=False, add_book=False)
app.display_alerts = False  # 关闭一些提示信息，可以加快运行速度。 默认为 True。
app.screen_updating = False  # 更新显示工作表的内容。默认为 True。关闭它也可以提升运行速度。

# 数据格式化存储
# 读取模板
file_path = './中台导出数据/test_file.xlsx'
wb = app.books.open(file_path)
# sheet = wb.sheets["填写sheet名字"] # 或者 sheet = wb.sheets["索引值从0开始"]

# 获取指定的表格
sheet = wb.sheets["供应商模板"]
# 数据读取指定文件sheet
value = sheet.range('A2').expand('right').value  # 第列名字行数据读取
print(value)

# 需要存储的数据读取
df_data = pd.read_excel('res.xlsx')

# 需要填写的名字数据获取
for column in ['货号*', '价格，USD*', '增值税，%*', '商业类型*',
               '毛重，克*', '包装宽度，毫米*', '包装高度， 毫米*', '包装长度，毫米*', '主照片的链接*',
               '部件号（制造商的货号）*', '品牌*', '类型*', '型号名称*']:
    try:
        num_x = value.index(column)  # 获取列位置
        print(df_data.columns)
        li_data_x = list(df_data[column].values)
        # 从第4行的第n列数据下都为
        sheet.range(4, num_x + 1).expand('down').options(transpose=True).value = li_data_x
    except:
        pass

# 数据存工作簿并且关闭工作簿
wb.save()
wb.close()
app.quit()
