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
sql = 'SELECT * FROM stuinfo WHERE 序号>%s'
cur.execute(sql,1)
results = cur.fetchall()
lst = []
for items in results:
    lst.append(items)

print(lst)

#关闭资源
cur.close()
conn.close()
