#list.sort 方法会就地排序列表
#与 list.sort 相反的是内置函数 sorted，它会新建一个列表作为返回值。
#这个方法可以接 受任何形式的可迭代对象作为参数
#而不管 sorted 接受的是怎样的参数，它最后都会返回一个列表。
fruits = ['grape', 'raspberry', 'apple', 'banana']
print(sorted(fruits,key=lambda a:a[1]))
