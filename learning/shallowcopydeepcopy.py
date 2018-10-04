old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 'a']]
new_list = old_list    #only creates reference of original objects

new_list[2][2] = 9

print('Old List:', old_list)
print('ID of Old List:', id(old_list))

print('New List:', new_list)
print('ID of New List:', id(new_list))

#As you can see from the output both variables old_list and new_list shares the same id i.e 140673303268168.
#So, if you want to modify any values in new_list or old_list, the change is visible in both.




#shallow copy example

import copy

old_list2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list2 = copy.copy(old_list2)
new_list2[2][2] = 100
old_list2[1][2]=2000      #affect both list as we made changes to old_list2 i.e old_list2[1][2] = 2000. Both sublists of old_list2 and new_list2 at index [1][2] were modified. This is because, both lists share the reference of same nested objects.
old_list2.append([22,33,44]) #we created a shallow copy of old_list2. The new_list2 contains references to original nested objects stored in old_list2. Then we add the new list i.e [22, 33, 44] into old_list. This new sublist was not copied in new_list2
new_list2.append([55,66])
old_list2[3][1]=8000       #nested object created after shallow copy so not copied in new list. so no change in new list
print("Old list2:", old_list2)
print('ID of Old List:', id(old_list2))
print("New list2:", new_list2)
print('ID of New List:', id(new_list2))


#A shallow copy creates a new object which stores the reference of the original elements.

#So, a shallow copy doesn't create a copy of nested objects, instead it just copies the reference of nested objects. This means, a copy process does not recurse or create copies of nested objects itself


#DEEP COPY   - A deep copy creates a new object and recursively adds the copies of nested objects present in the original elements.
old_list3 = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list3 = copy.deepcopy(old_list3)
old_list3[1][0] = 'BB'    #no changes to the copy new_list3
print("\n\nOld list3:", old_list3)
print('ID of Old List:', id(old_list3))
print("New list3:", new_list3)
print('ID of Old List:', id(new_list3))


#In the above program, when we assign a new value to old_list, we can see only the old_list is modified. This means, both the old_list and the new_list are independent. This is because the old_list was recursively copied, which is true for all its nested objects.

