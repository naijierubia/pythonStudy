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

sql = "select img from cls where name='Yuki';"
try:
    cur.execute(sql)
    pic = cur.fetchone()
    with open('Yuki_get.jpg', 'wb') as f:
        f.write(pic[0])
        f.close()
    print("success")
except:
    db.rollback()
    print("error")

# 关闭游标和数据库连接
cur.close()
db.close()
