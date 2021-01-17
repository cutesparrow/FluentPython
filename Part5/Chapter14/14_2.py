def generator():
    for i in range(10):
        print('ready to yield')
        b = yield i
        if b:
            print(b)
gen = generator()
result = gen.__next__()
print(result)
result = gen.send(10)
print(result)
print(next(gen))

# 每运行一次next 或者 send，就会运行直到完成yield一次，之后立刻停止，等待下一个send 或者next
