class Student(object):
    def __init__(self,name,score):
        self.__name=name
        self.__score=score
    def get_grade(self):
        if self.__score>=90:
            return 'A'
        if self.__score>=60:
            return 'B'
        if self.__score>=0:
            return 'C'
    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score
lisa = Student('Lisa',99)
bob = Student('Bob',60)
print(lisa.get_name(),lisa.get_grade(),lisa.get_score())
print(bob.get_name(),bob.get_grade(),bob.get_score())
