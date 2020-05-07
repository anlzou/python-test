from datetime import date

class Student():
    def __init__(self,student_id,name,brithday):
        self.student_id = student_id
        self.name = name
        self.brithday = brithday
    def getAge(self):
        year = int(self.brithday[0:4])
        age = date.today().year - int(year)
        return age

#主函数
student = Student('001','an','19961114')
print(student.student_id)
print(student.name)
print(student.brithday)
print(student.getAge())
