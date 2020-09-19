#
# @Date        : 2020-09-19 20:04:52
# @LastEditors : anlzou
# @Github      : https://github.com/anlzou
# @LastEditTime: 2020-09-19 20:59:45
# @FilePath    : \python\sqlit\sqlit-test1.py
# @Describe    :
#
import sqlite3


class test:
    def createTable(sql_create):
        '''连接数据库
            连接到一个现有的数据库。
            如果数据库不存在，那么它就会被创建，最后将返回一个数据库对象。
        '''
        conn = sqlite3.connect('./test.db')
        print('connect database successfully')

        '''创建表 create table
            1.创建游集
            execute：执行sql语句
            commit：提交操作
            2.关闭数据库
        '''
        cur = conn.cursor()
        cur.execute(sql_create)
        conn.commit()
        conn.close()

    def insertData(sql_insert):
        '''插入数据 insert into
        '''
        conn = sqlite3.connect('test.db')
        print('connect database successful')

        cur = conn.cursor()
        cur.execute(sql_insert)
        conn.commit()
        print('Records created successfully')

    def selectData(sql_select):
        '''SELECT 操作
        '''
        conn = sqlite3.connect('test.db')
        print("connected database successfully")
        cur = conn.cursor()

        datas = cur.execute(sql_select)
        for data in datas:
            print('id: ', data[0])
            print('name: ', data[1])
            print('age: ', data[2])
            print('address: ', data[3])
            print('sqlary: ', data[4])
        print("Operation done successfully")
        conn.close()

    def updateData(sql_update):
        '''UPDATE 操作
        '''
        conn = sqlite3.connect('test.db')
        print('connected database successfully')
        cur = conn.cursor()

        cur.execute(sql_update)
        conn.commit()
        print("Total number of rows updated :", conn.total_changes)
        print('Operation done successfully')
        conn.close()

    def deleteData(sql_delete):
        '''DELETE 操作
        '''
        conn = sqlite3.connect('test.db')
        print("connected database successfully")
        cur = conn.cursor()

        cur.execute(sql_delete)
        conn.commit()
        print("Total number of rows deleted :", conn.total_changes)
        print("Operation done successfully")
        conn.close()


##################test##################
sql_create = '''
        create table company(
            id int primary key not null,
            name text not null,
            age int not null,
            address char(50),
            salary real
        );
    '''
# test.createTable(sql_create)

sql_insert1 = "INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
    VALUES (1, 'Paul', 32, 'California', 20000.00 )"
sql_insert2 = "INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
    VALUES (2, 'Allen', 25, 'Texas', 15000.00 )"
sql_insert3 = "INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
    VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )"
sql_insert4 = "INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
    VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )"
# test.insertData(sql_insert1)
# test.insertData(sql_insert2)
# test.insertData(sql_insert3)
# test.insertData(sql_insert4)

sql_update = "update company set age = 4 where id = 1"
# test.updateData(sql_update)

sql_delete = "delete from company where id = 2"
# test.deleteData(sql_delete)

sql_select = "select * from company \
    "
# test.selectData(sql_select)
