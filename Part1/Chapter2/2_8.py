import bisect
a = [1,2,3,4,4,4,4,5,6,7,8,9]
b = 4
print(bisect.bisect(a,b))
#如果我们需要一个只包含数字的列表，那么 array.array 比 list 更高效
#memoryview 是一个内置类，它能让用户在不复制内容的情况下操作同一个数组的不同切 片。
#collections.deque 类(双向队列)是一个线程安全、可以快速从两端添加或者删除元素的 数据类型。而且如果想要有一种数据类型来存放“最近用到的几个元素”，deque 也是一个 很好的选择。

