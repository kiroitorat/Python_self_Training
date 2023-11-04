def min_abs_indices(s):
    '''
    [1,2,3,-1,-5]
    return [0, 3]'''
    '''方案一，使用map映射以及min函数找到绝对值最小的值是什么
    然后对比原数组， 返回索引'''
    min_abs = min(map(abs, s))
    return [i for i in range(len(s)) if abs(s[i]) == min_abs]
print(min_abs_indices([1,2,3,-1,-5]))

def largest_adi_sum(s):
    '''[-3,-6,1,5,2]
    return 7'''
    '''方案一m_1 = max(s)
    s.remove(m_1)
    m_2 = max(s)
    return m_1 + m_2
    '''
    
    '''方案二'''
    return max([a + b for a,b in zip(s[:-1], s[1:])])
print(largest_adi_sum([-3,-6,1,5,2]))

def digit_dict(s):
    return {d: [x for x in s if x%10 == d] for d in range(10) if any([x%10 == d for x in s])}
print(digit_dict([1,87,45,834,-4,65]))