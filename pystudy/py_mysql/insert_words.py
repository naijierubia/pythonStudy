"""
创建单词表
"""

import pymysql

# 链接数据库
db = pymysql.connect(host='localhost',
                     port=3306,
                     user="root",
                     password='perseus0709?',
                     charset='utf8',
                     database='books')

# 生成游标
cur = db.cursor()
args_list = []
with open('dict.txt') as f:
    for line in f:
        word, mean = line.split(' ', 1)
        args_list.append((word, mean.strip()))
    f.close()

sql = "insert into english_words (word,mean) values (%s,%s);"
try:
    cur.executemany(sql, args_list)
    db.commit()
    print("success")
except:
    db.rollback()
    print("error")

# 关闭游标和数据库连接
cur.close()
db.close()



