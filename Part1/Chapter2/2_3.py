#tuple
#元组中的每个元素都存放了记录中一个字段的数据，外加这个
#字段的位置。正是这个位置信息给数据赋予了意义。
traveler_ids = [('USA','31192394'),('BRA','CE849438'),('ESP','4KJ4443')]
for i,_ in traveler_ids:
    print(i)

t = [1,2,3,4,5]
def testIter(*t):
    for i in t:
        print(i)
testIter(*t)
#在 Python 中，函数用 *args 来获取不确定数量的参数算是一种经典写法了。
a,b,*rest = range(5)
print(a,b,rest)
from collections import namedtuple

Person = namedtuple('Person','name sex age height weight')
me = Person('ziven','male',18,188,100)
print(me.name)
me_data =('ziven','male',18,188,100) 
other = Person._make(me_data)
print(other._asdict())
other1 = Person(*me_data)
print(other1)
print(Person._fields)
a = [1,2,3,4,5,6]
b =slice(0,5,2)
print(a[b])
import dis
dis.dis('a.append(1)')
#• 不要把可变对象放在元组里面。
#• 增量赋值不是一个原子操作。我们刚才也看到了，它虽然抛出了异常，但还是完成了操作。 
#• 查看 Python 的字节码并不难，而且它对我们了解代码背后的运行机制很有帮助。

