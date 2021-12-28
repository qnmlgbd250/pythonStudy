# -*- coding: utf-8 -*-
# @Time    : 2021/12/27 18:38
# @Author  : sunfukai
# @Email   : zcshiyonghao@163.com
# @File    : mongoDB_test.py
# @Software: PyCharm
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient['test2']
# myclient = pymongo.MongoClient('localhost',27017)
print(myclient.list_database_names())

# import pymongo
# myclient = pymongo.MongoClient('localhost', 27017)
# db = mongo_client.admin
# db.authenticate('用户名', '密码')

# 获取数据库
db = myclient.test
print(db)
# 方法二：db = client['test']
# 指定集合
collection = db.stu
# 方法二：collection = db['stu']
stu1 = {'id': '001', 'name': 'zhangsan', 'age': 10}
result = collection.insert_one(stu1)

stu2 = {'id': '002', 'name': 'lisi', 'age': 15}
stu3 = {'id': '003', 'name': 'wangwu', 'age': 20}
result = collection.insert_many([stu2, stu3])

#update_one,第 2 个参数需要使用$类型操作符作为字典的键名
#姓名为zhangsan的记录，age修改为22
condition = {'name': 'zhangsan'}
res = collection.find_one(condition)
res['age'] = 22
result = collection.update_one(condition, {'$set': res})
print(result) #返回结果是UpdateResult类型
print(result.matched_count,result.modified_count) #获得匹配的数据条数1、影响的数据条数1

#update_many,所有年龄为15的name修改为xixi
condition = {'age': 15}
res = collection.find_one(condition)
result = collection.update_many(condition, {'$set':{'name':'xixi'}})
print(result) #返回结果是UpdateResult类型
print(result.matched_count,result.modified_count) #获得匹配的数据条数3、影响的数据条数3

rets = collection.find({"age":20})
for ret in rets:
    print(ret)
 # 查询结果有多少条数据
# count = collection.find().count()
 # 查询结果按年龄升序排序
results = collection.find().sort('age', pymongo.ASCENDING)
print([result['age'] for result in results])

rets =collection.find_one({'name': 'zhangsan'})
print(rets)
