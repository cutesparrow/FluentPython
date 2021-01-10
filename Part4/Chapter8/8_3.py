#复制列表(或多数内置的可变集合)最简单的方式是使用内置的类型构造方法。
a = [1,2,3,[1,2,3]]
b = list(a)
print(a is b)
#构造方法或 [:] 做的是浅复制(即复制了最外层容器，副本中的元素是源容器中元 素的引用)。如果所有元素都是不可变的，那么这样没有问题，还能节省内存。但是，如 果有可变的元素，可能就会导致意想不到的问题。
c = a[:]
print(id(a))
print(id(c))
print(id(a[-1]))
print(id(c[-1]))
print(id(b[-1]))
from copy import deepcopy,copy

