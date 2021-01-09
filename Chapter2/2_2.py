#列表推导和生成器表达式
i = 'abcdefg'
b = [ord(a) for a in i]
print(b)

#生成器表达式
import array
a = array.array('I',(ord(i) for i in i))
print(a)
