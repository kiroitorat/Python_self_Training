'''lambda function is a function that has no intrinsic name
    means it's a nameless function(be different to but similar the 匿名函数)
    
    1.Evaluating a lambda expression does not create or modify any variables.
    
    see some example :
    '''
    
def f(x):
    from math import radians
    return  radians(x*100)
    
def common_function_higher(f,operand):
    def operation(*args):
        return int(*args)**operand
    return operation

print(common_function_higher(f(5),2)(2))
'''then we use lambda expression'''
print(common_function_higher(lambda x: 9, 2)(2))

square = lambda x: x * x
print(square(3))

negate = lambda f, x: -f(x)
print(negate(lambda x: x * x, 3))

b = lambda x: lambda: x  # Lambdas can return other lambdas!
c = b(88)
print(c,'Error: this is a function')
print(c())