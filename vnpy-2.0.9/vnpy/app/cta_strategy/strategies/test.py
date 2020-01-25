class Student():
    age = 0
    name = 'stu'
    # age,name是类变量
    def __init__(self,age,name):
        self.age = age
        self.name = name

student1=Student(18,'zhoulibing')
print(student1.name)
print(Student.name)
Student.name='chengchen'
print(Student.name)
