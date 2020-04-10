# coding='utf-8'


"""
删除行：Ctrl+x
复制行：ctrl+shift+x
显示调试控制台：ctrl+shift+Y
资源管理器：ctrl+shift+E
搜索：ctrl+shift+F
运行和调试：ctrl+shift+D
Extension：ctrl+shift+X
设置：ctrl+，
拆分：ctrl+\
关闭窗口：ctrl+W
关闭编辑器：ctrl+F4
选择所有匹配项：ctrl+shift+L
转到括号：ctrl+shift+\
跳转到哪一行：ctrl+G
打开键盘快捷键设置页面：ctrl+1
打开新的外部终端：ctrl+shift+c
全部展开：ctrl+K,J
全部折叠：ctr+K,O
展开所有区域：ctrl+k+9
放大：ctrl+shift+=
在上面插入行：ctrl+shift+enter
注释代码块(""" """)：ctrl+shift+A
折叠所有文件夹：ctrl+shift+[]
格式化文档：alt+shift+F
 """
# from vnpy.app.cta_strategy.csv_backtesting import CsvBacktestingEngine, OptimizationSetting
from pathlib import Path
from datetime import datetime, timedelta
import os
import random
import math
import cmath
from pathlib import Path
import numpy as np
import pandas as pd
import time
from pymongo import MongoClient
from multiprocessing import Pool
from pymongo import MongoClient
import pymongo.errors as mongoerr
import matplotlib as mpl
import matplotlib.pyplot as plt
p = Path.cwd()
p_new = p / 'new_dir'
print(p_new)
# p_new.mkdir(parents=True)
parents1 = r'E:\guanlan'
print(p.is_absolute())
print(p.parents())
print(Path().parents(p))
Path(parents1).mkdir(parents=True)
# for py in path.rglob('*.py'):
#     print(py)
# print(str.encode(str))
# client = MongoClient(host='localhost', port=27017)  # 连接，host为地址，port为端口
# sz_stock_db = client.SZ_STOCK_DAILY_DB
# test_db=client.test_db
# start_time = datetime(2001, 3, 1)
# end_time = datetime(2001, 3, 20)
# bos=[]

# fig=plt.figure(figsize=(10, 16))
# ax1=plt.subplot(4, 1, 1)
# ax2=plt.subplot(4, 1, 2)
# ax3=plt.subplot(4, 1, 3)
# ax4=plt.subplot(4, 1, 4)
# plt.subplots_adjust(hspace=0.50)
# x=(np.random.randn(1200) - 0.5) * 1000
# y=1000000 + x



# ax1.set_title('Balance')
# ax2.set_title('Drawdown')
# ax3.set_title('Daily_PNL')
# ax4.set_title('net_PNL')

start=datetime(2015, 1, 1)
stop=datetime(2015, 1, 1) + timedelta(days=1200)
delta=timedelta(days=1) * 200

# dates=mpl.dates.drange(start,stop,delta)
# y = np.random.rand(len(dates))

date=[start, start + delta, start + delta * 2, start + \
    delta * 3, start + delta * 4, start + delta * 5]
ax1.plot(x, y)
ax1.set_xticks([0, 200, 400, 600, 800, 1000, 1200])
ax1.set_xticklabels(date)
plt.show()

fig1=plt.figure()
ax=fig1.add_subplot(111)
ax.plot_date(dates, y, linestyle='-', marker='')
date_format=mpl.dates.DateFormatter('%Y-%m')
ax.xaxis.set_major_formatter(date_format)
fig1.autofmt_xdate()
plt.show()


# addvalue = {"x": [{"a":1, "b":3}, 7, {"b":99}, {"a":11}]}
# # test_db.test.insert_one(addvalue)
# results_1 = test_db.test.find()
# test_db.test.save({ "title" : "My First Post", "author": {"name" : "Jane", "id" : 1}})
# # result_2 = test_db.test.find({x: {$elemMatch:{a:1,b:{$gt:1}}}})
# results_1 = test_db.test.find_one({"author.name"："Jane"})
# result_3 = test_db.test.find({"x.a": 1,"x.b":{$gt:1}})
# print(result_3)



#   #                   t.find({x: {$elemMatch:{a:1,b:{$gt:1}}}})
# print(result_2)
for result in results_1:
    print(result)
results=sz_stock_db['000001'].find({'datetime': start_time}, {
                                   '_id': 0, 'datetime': 1}).limit(10)
print(results)
for result in results:
    print(result)











client.adminCommand(
    'copydb',
    fromdb='client.test_db.test_1',
    todb='client.test_db_1.test1'
)


print(test_db.list_collection_names())
new_posts=[{"author": "Mike",
              "text": "Another post!",
              "tags": ["bulk", "insert"],
              "date": datetime(2009, 11, 12, 11, 14)},
             {"author": "Eliot",
              "title": "MongoDB is fun",
              "text": "and pretty easy too!",
              "date": datetime(2009, 11, 10, 10, 45)}]
result=test_db.test_1.insert_many(new_posts)
print(test_db.test_1.count_documents(
    {'author': 'Mike'}))  # 查询满足条件的documents有多少条

# print(result)
print(result.inserted_ids)
for post in test_db.test_1.find():
    print(post)
# print(collist)
print(dblist)
print(datetime.utcnow())
# （1）mongodb数据去重
"""
检查其中的数据是否存在重复项
"""
# client = MongoClient(host='localhost', port=27017)  # 连接数据库
# sz_stock_db = client.SZ_STOCK_DAILY_DB  # 连接collection

# list = []
# for document in cursor:
#     list.append(document)
# print(len(list))
# data = pd.DataFrame(list)
# # data['datetime']=data[['datetime']].applymap(lambda x:str(x).strftime("%Y-%m-%d %h:%M:%S"))

# # print(data.shape)
# print(data.dtypes)
# # data['datetime'] = data['datetime'].astype(datetime)
# # print(data.dtypes)
# data=data.sort_values(['datetime'], ascending=True, inplace=True)
# data.drop_duplicates(subset=['datetime'], keep='first', inplace=True)
# print(data.shape)
# print(data)

# （2）mongodb数据查漏
"""
思路：根据数据的级别，按级别进行检查，去除其中的节假日和休息日
"""

# （3）把csv数据导入mongodb

# 获取相关csv文件

# 连接数据库
try:
    client=MongoClient(host='localhost', port=27017)
except mongoerr.ConnectionFailure as e:
    print("Could not connect: %s" % e)


def get_filename(path: str):
    """
    遍历整个文件夹，获取所有的回测文件地址和文件名称列表
    """
    stock_code_list=[]
    filename_list=[]
    for dirpath, dirnames, filenames in os.walk(str(path)):
        # os.walk() 方法用于通过在目录树中游走输出在目录中的文件名
        for filename in filenames:
            # 判断交易所
            if filename.startswith("6") or filename.startswith("8"):
                stock_code=filename[:-4] + ".SH"
                stock_code_list.append(stock_code)
            else:
                stock_code=filename[:-4] + ".SZ"
                stock_code_list.append(stock_code)
            # 判断文件后缀
            if filename.endswith(".csv"):
                filename=path + "\\" + filename
                filename_list.append(filename)

    return stock_code_list, filename_list


# 连接mongodb和相关数据库
client=MongoClient(host='localhost', port=27017)  # 连接数据库
sz_stock_db=client.SZ_STOCK_DAILY_DB              # 连接collection
sh_stock_db=client.SH_STOCK_DAILY_DB
kc_stock_db=client.KC_STOCK_DAILY_DB
# csv数据地址
path='D:\\The Road For Finacial Statics\\Python\\02.Learning Materrials\\02.Data\\02.daily_BarData'
stock_code_list, filename_list=get_filename(path)
ix=0
n=len(filename_list)

while ix < n:
    print('loading_data ', ix + 1, '/', n)
    stock_code=stock_code_list[ix][:-3]

    # 获取并处理df数据 多余的数据需要处理603893
    df_all=pd.read_csv(filename_list[ix], parse_dates=["trade_date"])
    df_all.rename(
        columns={
            "trade_date": "datetime",
            "vol": "volume", },
        inplace=True
    )
    if 'Unnamed: 0' in df_all.columns:
        df_all=df_all.drop('Unnamed: 0', axis=1)
    df_all.sort_values(['datetime'], ascending=True, inplace=True)

    # 获取db文档最后数据日期
    rows=sz_stock_db[stock_code].find().sort('datetime', -1)
    try:
        last_date=next(rows)['datetime']
    except StopIteration:
        last_date=df_all['datetime'].min() - timedelta(hours=24)

    # 在mongodb中添加新的数据
    df_part=df_all[df_all['datetime'] > last_date]
    # df转化为dict
    dict_all=df_part.to_dict(orient='records')

    # 判断存入数据是否为空
    if dict_all == []:
        print('loading_data for [' + stock_code + '] has got.')
        ix += 1
        continue

    # 把数据存入mongodb
    if stock_code.startswith("6"):
        sh_stock_db[stock_code].insert_many(dict_all)
    elif stock_code.startswith("3") or\
            stock_code_list[ix].startswith("0"):
        sz_stock_db[stock_code].insert_many(dict_all)
    else:
        kc_stock_db[stock_code].insert_many(dict_all)

    ix += 1
    print('loading_data for [' + stock_code + '] got.')
client.close()


db=client.test_db  # 获取数据库实例
# minute_db = mc[MINUTE_DB_NAME]
# daily_db = mc[DAILY_DB_NAME]
dbcol=db["test"]  # 读取集合中的collection实例
# dbcol.drop()    #删除此collection
insert_doc={'name': 'test2', 'age': 30}
filter, update={"name": "test"}, {"$set": {"name": "test2"}}
db.test.update_one(filter, update)  # 插入一条数据
# db.test_1.insert_one(insert_doc)#插入一条数据
# print(db.test)

array=list(db.test.find())  # 查询collection中的数据，find找到的是迭代数据，可以用list转化为可见。
collist=db.list_collection_names()  # 查询数据库中的collection
dblist=client.list_database_names()  # 访问数据库列表
my_stock_daily_data=client.stock_daily_data
my_daily_col=my_stock_daily_data.data
for x in my_daily_col.find():  # 查询collection中的数据，查询一条是find_one()
    print(x)

for x in my_daily_col.find({}, {"_id": 0, "Timestamp": 1}).limit(5):
    # 除了 _id 你不能在一个对象中同时指定 0 和 1，如果你设置了一个字段为 0，则其他都为 1，反之亦然。
    print(x)
result=my_daily_col.find_one({"Timestamp": '2019/12/31 13:55'})
print(type(result))
print(result)
