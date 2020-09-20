#
# @Date        : 2020-09-19 22:28:48
# @LastEditors : anlzou
# @Github      : https://github.com/anlzou
# @LastEditTime: 2020-09-20 20:24:49
# @FilePath    : \python\mongoDB\mongoDB-test.py
# @Describe    :
#
import pymongo


class Test(object):
    def __init__(self, url, database_name):
        super().__init__()
        self.url = url
        self.database_name = database_name

    def createDatabase(self):
        '''创建一个数据库
            创建数据库需要使用 MongoClient 对象，
            并且指定连接的 URL 地址和要创建的数据库名。
            注意: 在 MongoDB 中，数据库只有在内容插入后才会创建! 就是说，数据库创建后要创建集合(数据表)并插入一个文档(记录)，数据库才会真正创建。
        '''
        myclient = pymongo.MongoClient(url)
        mydb = myclient[self.database_name]
        print("create database successful")

    def isExist_database(self, database_name):
        '''判断数据库是否存在
            注意: 在 MongoDB 中，数据库只有在内容插入后才会创建! 就是说，数据库创建后要创建集合(数据表)并插入一个文档(记录)，数据库才会真正创建。
        '''
        myclient = pymongo.MongoClient(self.url)

        dblist = myclient.list_database_names()
        if database_name in dblist:
            print('数据库 “'+database_name+"” 已经存在")
        else:
            print('数据库 “'+database_name+"” 未存在")

    def create_collcection(self, collection_name):
        '''创建集合
            MongoDB 中的集合类似 SQL 的表。
        '''
        myclient = pymongo.MongoClient(self.url)
        mydb = myclient[database_name]
        mycollection = mydb[collection_name]

        print("create collection successful")

    def isExist_collection(self, collection_name):
        '''判断集合是否存在
            注意: 在 MongoDB 中，数据库只有在内容插入后才会创建! 就是说，数据库创建后要创建集合(数据表)并插入一个文档(记录)，数据库才会真正创建。
        '''
        myclient = pymongo.MongoClient(self.url)

        mydb = myclient[self.database_name]

        collist = mydb.list_collection_names()

        if collection_name in collist:
            print('集合 “'+collection_name+"” 已经存在")
        else:
            print('集合 “'+collection_name+"” 未存在")


##########--main test--##########
url = 'mongodb://localhost:27017/'
database_name = 'pymongo-test'
collection_name = 'test'
test = Test(url, database_name)

# Test.createDatabase()
# test.isExist_database(database_name)
# test.create_collcection(collection_name)
# test.isExist_collection(collection_name)
