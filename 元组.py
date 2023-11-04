t1 = ([0, 1], 2, 'kiroitorat')
t2 = (1, 2, 3, "kiroitorat")
#元组是不可更改的列表,可以更改的只有可变对象，比如list
#string是不可更改对象
#比如

#t1[0] = 11 报错
t1[0][0] = 11 #正确，因为没有改变t1的第一个元素是二元list的事实


def my_map(fn, seq):
    """Applies fn onto each element in seq and returns a list.
    >>> my_map(lambda x: x*x, [1, 2, 3])
    [1, 4, 9]
    """
    for factor in range(len(seq)):
        seq[factor] = fn(seq[factor])
        
    return seq
    
def my_filter(pred, seq):
    """Keeps elements in seq only if they satisfy pred.
    >>> my_filter(lambda x: x % 2 == 0, [1, 2, 3, 4])  # new list has only even-valued elements
    [2, 4]
    """
    arr = []
    for factor in seq:
        if pred(factor):
           arr.append(factor)
    return arr 

def my_reduce(combiner, seq):
    """Combines elements in seq using combiner.
    seq will have at least one element.
    >>> my_reduce(lambda x, y: x + y, [1, 2, 3, 4])  # 1 + 2 + 3 + 4
    10
    >>> my_reduce(lambda x, y: x * y, [1, 2, 3, 4])  # 1 * 2 * 3 * 4
    24
    >>> my_reduce(lambda x, y: x * y, [4])
    4
    >>> my_reduce(lambda x, y: x + 2 * y, [1, 2, 3]) # (1 + 2 * 2) + 2 * 3
    11
    """
    "*** YOUR CODE HERE ***"
    
def count_palindromes(L):
    """The number of palindromic strings in the sequence of strings
    L (ignoring case).
    >>> count_palindromes(("Acme", "Madam", "Pivot", "Pip"))
    2
    >>> count_palindromes(["101", "rAcECaR", "much", "wow"])
    3
    """
    count = 0
    for factor in L:
        factor = str(factor).lower()
        if factor[::-1] == factor:
            count += 1
    return count

def max_path_sum(t):
    """Return the maximum path sum of the tree.

    >>> t = tree(1, [tree(5, [tree(1), tree(3)]), tree(10)])
    >>> max_path_sum(t)
    11
    """
    if label(t):
        return label(t)
    else:
        return label(t) + max([max_path_sum(b) for b in branches(t)])






print(count_palindromes(["101", "rAcECaR", "much", "wow"]))