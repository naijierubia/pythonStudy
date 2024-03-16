import pymongo

'''
无需提前创建数据库，无需手动提交到数据库执行
'''
nagato = {'name': '长门有希', 'character': '三无少女'}
# 创建数据库连接对象
conn = pymongo.MongoClient('localhost', 27017)
# 创建库对象
db = conn['testdb']
# 创建集合对象
myset = db['testset']
# 插入文档
myset.insert_one(nagato)

