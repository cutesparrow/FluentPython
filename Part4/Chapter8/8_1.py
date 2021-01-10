#变量是标注，而不是盒子。如果你不知道引用式变 量是什么，可以像这样对别人解释别名。
a = [1,2,3,4]
b = a
a.append(10)
print(b)
print(a is b)
# "is" is used to check if it is a alias
print('*' * 10)
c = [1,2,3,4,10]
print(a==c)
print(a is c)
d = None
print(d == None)
print(d is None)
#== 运算符比较两个对象的值(对象中保存的数据)，而 is 比较对象的标识。
#is 运算符比 == 速度快，因为它不能重载，所以 Python 不用寻找并调用特殊方法，而是直 接比较两个整数ID。而a == b是语法糖，等同于a.__eq__(b)。继承自object的__eq__ 方法比较两个对象的 ID，结果与 is 一样。但是多数内置类型使用更有意义的方式覆盖了 __eq__ 方法，会考虑对象属性的值。相等性测试可能涉及大量处理工作，例如，比较大型 集合或嵌套层级深的结构时。
