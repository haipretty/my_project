
import sqlite3

conn = sqlite3.connect('test.db')
print("数据库打开成功")

c = conn.cursor()

# sql = '''create table company (
#     id int primary key not null,
#     name text not null,
#     age int not null,
#     address char(50),
#     salary real
# );'''
# c.execute(sql)
# print("数据表创建成功")

# conn.commit()
# conn.close()

c.execute('''insert into company values (1, 'Paul', 32, 'California', 20000);''')
c.execute("select * from company;")
print(c.fetchall())
