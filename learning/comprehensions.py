#LIST comprehensions

list1=[1,2,3,9]
list2=[7,8,9,10]

########## MAP function #######
print("MAP",list(map(lambda x,y:x+y,list1,list2)))
print("MAP",list(map(lambda x:x+10,list1)))
def addition(n):
    return n + n
print("MAP",list(map(addition,list1)))


# List of strings
l = ['sat', 'bat', 'cat', 'mat']
test=list((map(list,l)))
print("MAP",test)
print("MAP",test)
print("MAP",list(l[0]))
########################## MAP ends #############

newlist=[i for i in range(10) if i>=4]
print("LIST COMPREHENSION",newlist)

squared=[x**2 for x in range(20)]
print("LIST COMPREHENSION",squared)


############# SET comprehension
#They are also similar to list comprehensions. The only difference is that they use braces {}

squared={x**2 for x in range(10)}
print("SET COMPREHENSION",squared)

########## generator comprehension
#They are also similar to list comprehensions. The only difference is that they don’t allocate memory for the whole list but generate one item at a time, thus more memory effecient.

multiples_gen = (i for i in range(30) if i % 3 == 0)
print(multiples_gen)
for x in multiples_gen:
    print(x)


################ genrator ends#######

####### map begins
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]

result = map(lambda x, y: x + y, numbers1, numbers2)
print("NEW",list(result))
print("NEW ",list(result))    # output is [] why ?
##Why printing again : print(list(result)) gives output : [] and not the list ?
#Because the map function returns an iterator. Once the iterator is exhausted it will not restart from the beginning. Think of it like the result will be the pointer to the 1st element. You go to the next using next(result) or in your case list(result) will fetch all the element from the iterator and move the pointer next to the last.

######################## map ends
# create a list of 2-tuples like (number, square)
print ([(x, x**2) for x in range(6)])

# flatten a list using a listcomp with two 'for'
vec = [[1,2,3], [4,5,6], [7,8,9]]
print([num for elem in vec for num in elem])


#[1, 2, 3, 4, 5, 6, 7, 8, 9]


########## tuple packing  in to variables
t = 12345, 54321, 'hello!'

x,y,z=t
print(x,y,z)
