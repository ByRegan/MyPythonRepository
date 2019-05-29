class Student(object):
    def __init__(self,age,sex):
        self.age=age
        self.sex=sex
    def paoniu(self):
        print("you can paoniu")
    def eat(self):
        print("you can eat")

zhangsan=Student(19,"male")
lishi=Student(18,"female")

zhangsan.paoniu()
lishi.eat()
