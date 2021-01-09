#使用 dir 函数可以探知 factorial 具有下述属性
def name(name):
    return name
#use inspect model to discribe funtion
from inspect import signature
sig = signature(name)
print(str(sig))
print(sig.parameters)
print(sig.parameters.items())
