#
# @Date        : 2020-09-20 20:25:25
# @LastEditors : anlzou
# @Github      : https://github.com/anlzou
# @LastEditTime: 2020-09-20 21:48:14
# @FilePath    : \python\mongoDB\mongoDb-4baseOperation.py
# @Describe    :
#
import pymongo


class Test(object):
    def __init__(self, url, database_name):
        super().__init__()
        self.url = url
        self.database_name = database_name

    def insertData(self, collection_name, insert_data):
        '''插入
            更多：https://www.runoob.com/python3/python-mongodb-insert-document.html
        '''
        myclient = pymongo.MongoClient(self.url)
        mydb = myclient[self.database_name]
        mycollcetion = mydb[collection_name]

        mycollcetion.insert_many(insert_data)
        print('collection inserted successful')

    def selectData(self, collection_name, select_key):
        '''查询
            更多：https://www.runoob.com/python3/python-mongodb-query-document.html
        '''
        myclient = pymongo.MongoClient(self.url)
        mydb = myclient[self.database_name]
        mycollcetion = mydb[collection_name]

        x = mycollcetion.find(select_key)
        for i in x:
            print(i)

    def updateData(self, collection_name, updata_key, update_data):
        '''更新数据
            更多：https://www.runoob.com/python3/python-mongodb-update-document.html
        '''
        myclient = pymongo.MongoClient(self.url)
        mydb = myclient[self.database_name]
        mycollcetion = mydb[collection_name]

        mycollcetion.update_many(updata_key, update_data)
        print("database updated successful")

    def deleteData(self, collection_name, delete_key):
        '''删除数据
            更多：https://www.runoob.com/python3/python-mongodb-delete-document.html
        '''
        myclient = pymongo.MongoClient(self.url)
        mydb = myclient[self.database_name]
        mycollcetion = mydb[collection_name]

        mycollcetion.delete_many(delete_key)
        print("database deleted successful")

    def sortData(self, collection_name, sort_key, rule):
        '''数据排序
            升序：rule = 1,默认
            降序：rule = -1
            anlzou-tips:排序并未commit
        '''
        myclient = pymongo.MongoClient(self.url)
        mydb = myclient[self.database_name]
        mycollcetion = mydb[collection_name]

        x = mycollcetion.find().sort(sort_key, rule)
        for i in x:
            print(i)
        print("database sorted sucessfull")


###############--main test--###############
if __name__ == "__main__":
    url = 'mongodb://localhost:27017/'
    database_name = 'pymongo-test'
    collection_name = 'test'
    test = Test(url, database_name)

    # 插入数据
    insert_data = [
        {"name": "an1", "age": 19, "sex": "boy"},
        {"name": "an2", "age": 18, "sex": "boy"},
        {"name": "an3", "age": 19, "sex": "boy"},
        {"name": "an4", "age": 20, "sex": "boy"}
    ]
    # test.insertData(collection_name, insert_data)

    # 更新数据
    update_key = {"name": "an"}
    update_data = {"$set": {"sex": "girl"}}
    # test.updateData(collection_name, update_key, update_data)

    # 删除数据
    delete_key = {"age": 18}
    # test.deleteData(collection_name, delete_key)

    # 数据排序
    sort_key = "age"
    test.sortData(collection_name, sort_key, 1)

    # 查询数据
    # select_key = {"name": 'an'}
    select_key = {}
    test.selectData(collection_name, select_key)
