import pymysql
#创建连接对象
conn = pymysql.connect(host="localhost",user="root",password="root",port=3306,database="tpshop2.0")
#创建游标
cursor = conn.cursor()
#执行SQL
cursor.execute("select version()")
result = cursor.fetchall()
print(result)
#关闭游标
cursor.close()
#关闭连接对象
conn.close()