#特殊方法的存在是为了被 Python 解释器调用的，你自己并不需要调用它 们。也就是说没有 my_object.__len__() 这种写法，而应该使用 len(my_object)
#然而如果是 Python 内置的类型，比如列表(list)、字符串(str)、字节序列(bytearray) 等，那么 CPython 会抄个近路，__len__ 实际上会直接返回 PyVarObject 里的 ob_size 属 性。PyVarObject 是表示内存中长度可变的内置对象的 C 语言结构体。直接读取这个值比 调用一个方法要快很多。


class Queue:
    def __init__(self, nums):
        self._nums = nums

    def __iter__(self):
        for i in self._nums:
            yield i


def testQueue():
    queue = Queue([1, 2, 3, 4, 5])
    for i in queue:
        print(i)


from math import hypot


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    '''
    交互式控制台和调试程序(debugger)用 repr 函数来获取字符串表示形式.
    __repr__ 和 __str__ 的区别在于，后者是在 str() 函数被使用，或是在
    用 print 函数打印 一个对象的时候才被调用的，并且它返回的字符串对
    终端用户更友好。
    '''

    def __repr__(self):
        return "Vector({},{})".format(self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    '''
    中缀运算符的基本原则就是不改变操作对 象，而是产出一个新的值
    '''

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

def testVector():
    vector = Vector(3,4)
    print(abs(vector))
    print(bool(vector))
    vector2 = Vector(0,0)
    print(bool(vector2))
    


testVector()
