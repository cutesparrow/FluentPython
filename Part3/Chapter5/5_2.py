#接受函数为参数，或者把函数作为结果返回的函数是高阶函数
name = ['ziven', 'gaoyushi', 'collins']
sortedName = sorted(name, key=lambda a: len(a))
print(sortedName)
def findDetail(**detail):
    print(detail)

findDetail(name='ziven',age='18')
