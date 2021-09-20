# 2021年8月 Python

import pymysql
DBhost='127.0.0.1'
DBuser='root'
DBpwd = '1234566'
DBname= '74student'
db = pymysql.Connect(host=DBhost,user=DBuser,password=DBpwd,database=DBname)
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

#sql = 'SELECT *  FROM STUINFO'
      # 使用 execute()  方法执行 SQL 查询
sql = "UPDATE STUINFO SET 性别 = '男' WHERE 序号=1"
try:
    cursor.execute(sql)
    db.commit()

except:
        db.rollback()

#cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取单条数据.
#data = cursor.fetchone()

cursor.execute('SELECT 家庭住址,COUNT(*) 数量 '
               'FROM STUINFO '
               'WHERE 序号<40 '
               'GROUP BY 家庭住址 '
               'HAVING 数量>1 '
               'ORDER BY 数量 '
               'DESC')
results = cursor.fetchall()
for row in results:
      print(row)

#print("Database version : %s " % data)

# 关闭数据库连接
cursor.close()
db.close()