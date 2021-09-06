import itertools
import numpy as np

def flattenList(arrayList):
    # flatten = list(itertools.chain(*arrayList))
    flatten = sum(arrayList, [])
    return (flatten)
    # return (list(numpy.concatenate(flatten)))

# el = [[1,2,3],[4,5,6],[7,8,9]]
el = [6, 2, [4, 3],[[[5], nil], 1]]
print(flattenList(el))