print("Hello World !")
my_list = [1,2,3,4,5]
number = 6
my_list.append(number)
print(my_list)
 
my_list = [1,2,3,4,5]
number = [6]
my_list = my_list + [number]
print(my_list)

my_list = [1,2,3,4,5]
my_list += [6]
print(my_list)

#step 4 extend
my_list = [1,2,3,4,5]
my_list.extend([6])
print(my_list)

#step 5 insert
my_list = [1,2,3,4,5]
#      0,1,2,3,4
print(my_list[3])

my_list = [1,2,3,4,5]
my_list.insert(len(my_list),6)
print(my_list)

#step six
#unpacking
# 3.5 python
my_list = [1,2,3,4,5]
my_list = [*my_list,6]
print(my_list)

#step 7
#internal method/list add
#روش داخلی
my_list = [1,2,3,4,5]
my_list = my_list.__add__([6])
print(my_list)

#step 8
#slicing
my_list = [1,2,3,4,5]
my_list[len(my_list):] = [6,7]
print(my_list)

#step 9
#operator
import operator
my_list = [1,2,3,4,5]
operator.iadd(my_list,[6,7,8])
print(my_list)

#step 10
#chain
from itertools import chain
my_list = [1,2,3,4,5]
my_list = list(chain(my_list, [6,7,8]))
print(my_list)

#step 10+
from itertools import chain
a = [1,2,3]
b = [4,5,6]
c = [7,8,9]
result = chain(a,b,c)
print(list(result))

#step 11
#for
my_list = [1,2,3,4,5]
for i in [6,7,8]:
    my_list.append(i)
    print(my_list)
    