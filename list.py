arr = [1,5,9,3,8,5]

def count_elements_in_arr(arr, element):
    total = 0
    
    for elements in arr:
        if elements == element:
            total += 1
    
    return total


'''range函数的用法，可以创造list，可以列出范围'''
print(list(range(5)))
print(range(5))


print([i+1 for i in arr])

'''切片slicing:用于取list的范围'''

a = [0,1,2,3,4,5]
print(a[1:3])
print(a[:1])
print(a[0:])


exec('print("hello!")')