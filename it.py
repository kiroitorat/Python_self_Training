kiroitorat = ['k', 'i', 'r', 'o','itorat']

turn_into_BIG = lambda x: x.upper()

#map接受的函数是延迟操作，是一个映射,只有当进行迭代的时候才会进行函数操作
it_1 = map(turn_into_BIG, kiroitorat)
print(list(it_1)) 
print(list(it_1))#第二次因为迭代完了所以是空的


{}
iter
list#列出list
zip#用于结合两个list的索引相同的元素，成为一个多元元素
filter#接受条件函数，对list进行条件判断
