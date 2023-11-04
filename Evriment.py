def square(x):
    return x**2

def twice_call_funticon(f,x):
    return f(f(x))

print(twice_call_funticon(square,2))#2**4
print(twice_call_funticon(lambda x: x**2, 2))#the same expression!
'''lambda expression can replace a function , and return a expression
    lambda (x) : x**2 equals to def f(x): return x**2
'''

'''next change its behavior!'''

def twice_call(x):
    def f(n):
        return n**2
    return f

from math import radians
anyone = radians(radians(radians(1)))
print(twice_call(anyone)(4))#anyone can be anything,it doesn't change the result 4**2

def make_adder(adder):
    def add_to(factor):
        return adder + factor
    return add_to

add_8 = make_adder(8)
'''
adder is setted to be 8
and 10 is being added'''
print(add_8(10))