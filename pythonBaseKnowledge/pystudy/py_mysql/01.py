"""
mysql 流程
"""

import pymysql

# 链接数据库
db = pymysql.connect(host='localhost',
                     port=3306,
                     user="root",
                     password='perseus0709?',
                     charset='utf8')

# 生成游标
cur = db.cursor()

# 执行语句
print(cur)

# 关闭游标和数据库
cur.close()
db.close()
