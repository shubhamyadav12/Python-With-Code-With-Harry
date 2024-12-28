from functools import reduce

l = [1, 2, 3453, 432, 3242]


def greater(a,b):
    if (a>b):
        return a
    return b
print(reduce(greater, l))