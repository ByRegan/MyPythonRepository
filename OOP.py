class Person(object):
    def __init__(self,hight,weight,age):
        self.hight = hight
        self.weight = weight
        self.age = age
    def paoniu(self):
        print('你现在拥有泡妞的技能')
    def eat(self):
        print("you can eat")

zhangsan=Person(170,50,29)
lishi = Person(180,70,22)

zhangsan.paoniu()
lishi.eat()
