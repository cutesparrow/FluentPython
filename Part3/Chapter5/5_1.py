#一等对象
#• 在运行时创建
#• 能赋值给变量或数据结构中的元素
#• 能作为参数传给函数
#• 能作为函数的返回结果
def factorial(n):
    '''return n!'''
    return 1 if n == 1 else n * factorial(n - 1)


print(factorial.__doc__)
print(type(factorial))
#__doc__ 属性用于生成对象的帮助文本
print(help(factorial))

#map function
def square(n):
    return n ** 2

a = range(10)
print(list(map(square,a)))
