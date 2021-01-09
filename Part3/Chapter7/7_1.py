#函数的装饰器和闭包
def outFunc():
    nameList = ['ziven', 'gaoyushi']

    def innerFunc(name):
        nameList.append(name)
        print(nameList)

    return innerFunc

def deco(func):
    print('running deco')
    def inner():
        print('running inner')
    return inner

@deco
def target():
    print('running target')

#target()
#装饰器的一大特性是，能把被装饰的函数替换成其他函数。第二个特性是，装饰器 在加载模块时立即执行。下一节会说明。
def func(*args):
    print(args)

