print("Welcome !")
#copy
lst = [1,2,3]
new_list = lst.copy()
new_list.append(4)
print("Original list:", list)
print("new list:", new_list)

my_list = [1,2,3,4,5]
my_list[len(my_list):] = [6,7]
print(my_list)
