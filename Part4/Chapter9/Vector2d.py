from array import array
import math


class Vector2d:
    typecode = 'd'

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __iter__(self):
        for i in (self.x, self.y):
            yield i

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r},{!r})'.format(class_name, *self)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
                bytes(array(self.typecode, self)))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    @classmethod
    def frombytes(cls,octets):
        typecode = chr(octets[0])
        print(typecode)
        print(memoryview(octets)[0])
        memv = memoryview(octets[1:]).cast(typecode)
        print(memv[0])
        return cls(*memv)

a = Vector2d(3,4)
b = bytes(a)
c = Vector2d.frombytes(b)
print(c)
# hashable need implement __hash__ and __eq__
#名称改写是一种安全措施，不能保证万无一失:它的目的是避免意外访问，不能防止故意 做错事
# add __ in the front of propoty

