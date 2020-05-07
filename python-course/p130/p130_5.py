import types
class Person(object):
    def __init__(self,person_id,age,name):
        self.setId(person_id)
        self.setAge(age)
        self.setName(name)
    def setId(self,person_id):
        if type(person_id) != str:
            print('年龄必须是字符串。')
            return
        self.person_id = person_id
    def setAge(self,age):
        if type(age) != int:
            print('年龄必须是整形。')
            return
        self.age = age
    def setName(self,name):
        if type(name) != str:
            print('名字必须是字符串。')
            return
        self.name = name
    def show(self):
        print('ID:',self.person_id,' 年龄:',self.age,' 名字:',self.name)
        
class Conservator(Person):
    def __init__(self,person_id,age,name,salary):
        Person.__init__(self,person_id,age,name)
        self.salary = salary
    def show(self):
        print('ID:',self.person_id,' 年龄:',self.age,' 名字:',self.name,' 工资:',self.salary)

class Student(Person):
    borrow_booksAndDate = {}
    def __init__(self,person_id,age,name,borrow_booksAndDate):
        Person.__init__(self,person_id,age,name)
        self.setBorrowbBoksAndDate(borrow_booksAndDate)
    def setBorrowbBoksAndDate(self,borrow_booksAndDate):
        self.borrow_booksAndDate.update(borrow_booksAndDate)
    def show(self):
        print('ID:',self.person_id,' 年龄:',self.age,' 名字:',self.name,' 借书信息:',self.borrow_booksAndDate)

#主程序
conservator = Conservator('con001',20,'angel',3000)
conservator.show()

dict = {'安徒生童话故事':'11月13日','C++':'11月13日'}
student = Student('stu001',19,'an',dict)
student.show()
