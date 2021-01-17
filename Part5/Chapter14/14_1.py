class Class:
    def __init__(self,students):
        self.students = students
    def __iter__(self):
        print('Int')
        return ClassIterator(self.students)

class ClassIterator:
    def __init__(self,students):
        self.students = students
        self.index = 0
    def __iter__(self):
        print('iterator once')
        return self
    def __next__(self):
        try:
            student = self.students[self.index]
        except IndexError:
            raise StopIteration()
        self.index+=1
        return student
from random import randint
def test():
    return randint(1,6)
a = iter(test,1)
for i in a:
    print(i)

