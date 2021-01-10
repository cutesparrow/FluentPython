#weak ref
def changeValue(nums):
    nums[0] += 1
    return nums[0]
a = [1,2,3,4]
print(id(a[0]))
changeValue(a)
print(id(a[0]))
print(a)
# 其实list可变的原因是：list保存的是各个元素的引用，而int等不可变的原因是：当他的值改变的时候引用指向下一位并且计算出应该的值。相当与复制了一次。
#https://www.jianshu.com/p/c5582e23b26c
