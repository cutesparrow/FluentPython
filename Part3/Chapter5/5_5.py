#不仅 Python 函数是真正的对象，任何 Python 对象都可以表现得像函数。为此，只需实现
#实例方法 __call__。
class Person:
    def __init__(self,name,age,sex):
        self._name = name
        self._age = age
        self._sex = sex
    def __call__(self):
        return self._name + self._age + self._sex
person = Person('ziven','18','male')
print(person())
print(callable(person))
