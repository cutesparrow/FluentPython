import weakref
s1 = {1,2,3} 
s2 = s1
def bye():
    print('gone')
ender = weakref.finalize(s2,bye)
print(ender.alive)
del s1
print(ender.alive)
del s2
print(ender.alive)
