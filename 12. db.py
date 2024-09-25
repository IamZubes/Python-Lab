import pymysql

db = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    database='test'
)

cursor = db.cursor()

create = 'CREATE TABLE EMPLOYEE(NAME CHAR(25), AGE INT(3), SALARY INT(10));'
insert1 = 'INSERT INTO EMPLOYEE VALUES("Zubin", 19, 10000)'
insert2 = 'INSERT INTO EMPLOYEE VALUES("Nandu", 20, 10000)'
insert3 = 'INSERT INTO EMPLOYEE VALUES("Ashil", 19, 10000)'
drop = 'DROP TABLE EMPLOYEE'

cursor.execute(create)
cursor.execute(insert1)
cursor.execute(insert2)
cursor.execute(insert3)
# cursor.execute(drop)
