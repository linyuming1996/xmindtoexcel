#导入包
import pymysql
#创建连接
conn = pymysql.connect(host='localhost',
                       port=3306,
                       user='root',
                       password='root',
                       database='books')
#获取游标对象
cursor = conn.cursor()
#执行SQL
sql = "select id, title, `read`, `comment` from t_book;"
cursor.execute(sql)
#获取查询结果的总记录数
print("获取的查询结果记录行数为：",cursor.rowcount)
#获取查询结果的第一条数据
print(cursor.fetchone())
#获取查询结果的所有数据
#重置游标
cursor.rownumber = 0
print(cursor.fetchall())
#获取查询结果的多条数据
#print(cursor.fetchmany(size=3))
#关闭游标
cursor.close()
#关闭连接
conn.close()

