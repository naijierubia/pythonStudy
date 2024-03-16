"""
小文件 小于65kb
"""

import pymysql

# 链接数据库
db = pymysql.connect(host='localhost',
                     port=3306,
                     user="root",
                     password='perseus0709?',
                     database='stu',
                     charset='utf8'
                     )
cur = db.cursor()
with open('yuki.jpg', 'rb') as f:
    pic = f.read()
    f.close()

sql = "update cls set img=%s where name='Yuki';"
try:
    cur.execute(sql, [pic])
    db.commit()
    print("success")
except:
    db.rollback()
    print("error")

# 关闭游标和数据库连接
cur.close()
db.close()
