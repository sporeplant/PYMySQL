# 2021年8月 Python 自学
# 2021年8月 Python 自学
#导入模块
import pymysql
#建立链接
conn = pymysql.connect(
    host='localhost',
    database='stu',
    user='root',
    passwd='1234566',
    charset='utf8')
#获取游标
cur = conn.cursor(pymysql.cursors.DictCursor)
#执行sql语句
    #sql = "CREATE TABLE usrinfo (id int(5) NOT NULL," \
    #      "user varchar(20) not null," \
    #      "pwd varchar(8) not null)"
#sql = 'insert into usrinfo (id,user,pwd) ' \
#      'values(%s,%s,%s)'
#cur.executemany(sql,[(1,'user1','1111'),(2,'user2','222'),(3,'user3','333')])
for i in range(1,10):
    id=1000*i+i
    passwd=111*i
    user='user'+str(i)
    i+=1
    sql = "insert into usrinfo (id,user,pwd) " \
          "values(%s,%s,%s)"
    cur.execute(sql,(id,user,passwd))

#关闭资源
conn.commit()

sql ='select * from usrinfo'
cur.execute(sql)
results=cur.fetchall()
for items in results:
    print(items)
cur.close()
conn.close()