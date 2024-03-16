"""
mysql write
"""

import pymysql

# 链接数据库
db = pymysql.connect(host='localhost',
                     port=3306,
                     user="root",
                     password='perseus0709?',
                     charset='utf8',
                     database='stu')

# 生成游标
cur = db.cursor()
name = input('Name:')
age = input('Age:')
sex = input('Sex:')
score = input('Score:')
# 执行语句 操作用try执行
try:
    # sql01 = "insert into cls (name,age,sex,score) values ('kyo', 17, 'm', 68)"
    # cur.execute(sql01)
    sql02 = "insert into cls (name,age,sex,score) values (%s,%s,%s,%s)"
    cur.execute(sql02, [name, age, sex, score])
    db.commit()
    print("success")
except Exception as e:
    print("error")
    db.rollback()  # 出错回滚数据

# 关闭游标和数据库
cur.close()
db.close()
