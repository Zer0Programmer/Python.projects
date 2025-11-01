import itertools
my_list = [1,2,3]
lazy_gen = (x for x in itertools.chain(my_list,[4,5]))
print(lazy_gen)
print(list(lazy_gen))

''''''

#in place
#append
lst = [1,2,3]
lst.append(4)
print(lst)

lst = [1,2,3]
lst.extend(4)
print(lst)

lst = [1,2,3]
lst_second = [4,5]
lst.insert(len(lst), 4)
print(lst)

# collections.dequecollections.deque
from collections import deque

dq = deque([1, 2, 3])
dq.append(4)   
print(dq)

# numpy.array
import numpy as np

arr = np.array([1, 2, 3])
arr = np.append(arr, 4)   #new list
print(arr)