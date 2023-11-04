#Generator生成器是特殊的迭代器
#yield 是协程实现的基础
#协程就是食堂阿姨打饭同学点菜但是很犹豫，于是张贴告示，告诉犹豫的同学点一个菜之后不要站在那里，直接到队伍的最后面去，想第二个菜吃什么
#send函数可以给生成器传递信息，temp=yield expression  (推荐：既可以返回迭代的值，也可以接受send进去的参数并使用)
def gen_f_plus_1(x):
    yield x+1#yield意味着产出，也就是自定义的迭代对象
    yield x+2
    
    
gen_it = gen_f_plus_1(1)
print(next(gen_it))
print(next(gen_it))


'''
简单地说，yield from  generator 。实际上就是返回另外一个生成器。而yield只是返回一个元素。
从这个层面来说，有下面的等价关系：yield from iterable本质上等于 for item in iterable: yield item 。'''
def a_b(a, b):
    yield from a
    yield from b
    
def a_and_b(a, b):
    for x in a:
        yield x
    for y in b:
        yield y
#a_b 和 a_and_b是等价的


def c_and_d(c, d):
    Value_c = yield c
    Value_b = yield d


def main():
    my_gen = c_and_d(6, 66)
    for i in my_gen:
        if i != 3:
            print(i)
            print(my_gen.send(3))
        else:
            print('back to')


main()

class Kiroitorat:
    def __init__(self, source):#__init__就是构造函数
        self.animation = source
        self.age = 18

kiroitorat = Kiroitorat("刀剑神域")

print(kiroitorat.animation)

print(hasattr(kiroitorat,'anmation'))#hasattr检查对象是否具有某一个属性， attribute是属性的意思
