my_list = [1,2,3]
my_list.append(4)
print(my_list)

my_list = [1,2,3]
my_list.extend([4,5])
print(my_list)

my_list = [1,2,3]
my_list += [4,5]
print(my_list)

my_list = [1,2,3]
my_list.insert(len(my_list), 4)
print(my_list)

my_list = [1,2,3]
new_list = my_list + [4,5]
print(my_list)
print(new_list)

my_list = [1,2,3]
new_list = [*my_list, 4, 5]
print(new_list)

my_list = [1,2,3]
new_list = list(my_list) + [4]
print(new_list)

lst = [1,2,3]
new_list = lst.copy()
new_list.append(4)
print(lst)
print(new_list)

import itertools
lst = [1,2,3]
new_list = list(itertools.chain(lst, [4,5]))
print(lst)
print(new_list)