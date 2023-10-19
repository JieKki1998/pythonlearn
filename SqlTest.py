import mysql.connector
#mydb用于获取数据库连接
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123456"
)
#mycursor用于执行sql命令
mycursor=mydb.cursor()
# mycursor.execute("create database test1")
#执行查看当前连接中所有的数据库
mycursor.execute("show databases")

for x in mycursor:
    print(x)

# 连接到指定数据库
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123456",
    database="test1"
)
mycursor=mydb.cursor()
mycursor.execute("show tables")
print("1tables:")
for x in mycursor:
    print(x,end="")

# mycursor.execute("CREATE TABLE table1 (id int(10),name varchar(10),passwd varchar(10))")
#sql语法：create table 表名(字段1名 字段1类型,字段2名 字段2类型,字段3名 字段3类型);
# mycursor = mydb.cursor()
print("2tables:")
for x in mycursor:
    print(x,end="")
#添加新字段my_key_id并设为主键
# mycursor.execute("alter table table1 add column   my_key_id int auto_increment primary key")

#startstartstartstartstart插入数据操作插入数据操作插入数据操作插入数据操作插入数据操作插入数据操作插入数据操作startstartstartstartstart
sql = "insert into table1 (id,name, passwd) values ('1','admin','123456')"
mycursor.execute(sql)
#或者写成:
sql = "insert into table1 (id,name,passwd) values (%s,%s,%s)"
val = (1,'abc','123')
mycursor.execute(sql,val)
#请注意语句 mydb.commit()。需要进行更改，否则表不会有任何改变。
mydb.commit()
#mycursor.rowcount返回的是当前数据库操作受影响行数
mycursor.rowcount
print(mycursor.rowcount, "record inserted.")
#endendendendendendendendend插入数据操作endendendendend插入数据操作endendendendendendendend插入数据操作endendendendendendend