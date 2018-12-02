

t=(1,2,3,4)
t1=1,


print(t1)
print(t)
################

#nested tuple  and mutuable nested element can be reassigned


t3=('mouse',[1,2,3],('cat','boll'))

#t3[0]=9 # gives error as tuple can not be reassigned
t3[1][0]=8 # no error as nested list in tuple can be change
#3[2][0]=100 #nested tuple can not be reassigned
print(t3)

# but item of mutable element can be changed



####################
my_tuple = 3, 4.6, "dog"
print(my_tuple)

# tuple unpacking is also possible
# Output:
# 3
# 4.6
# dog
a, b, c = my_tuple
print(a)
print(b)
print(c)

my_tuple = ("hello",)
print(type(my_tuple))   #type tell you type of class object

# parentheses is optional
# Output: <class 'tuple'>
my_tuple = "hello",
print(type(my_tuple))



#########slicing #####

my_tuple = ('p','r','o','g','r','a','m','i','z')

# elements 2nd to 4th
# Output: ('r', 'o', 'g')
print(my_tuple[1:4])


# elements beginning to end
# Output: ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
print(my_tuple[:])


#########We can also assign a tuple to different values (reassignment).
my_tuple = ('p','r','o','g','r','a','m')

#### addition or concatination
print((1, 2, 3) + (4, 5, 6))

# Output: ('Repeat', 'Repeat', 'Repeat')
print(("Repeat",) * 3)

#But deleting a tuple entirely is possible using the keyword del.
del my_tuple
#print(my_tuple)

########
my_tuple = ('a','p','p','l','e',)

# Count
# Output: 2
print(my_tuple.count('p'))

# Index
# Output: 3
print(my_tuple.index('l'))
print('a' in my_tuple)
############# iteration

for name in ('John','Kate'):
     print("Hello",name)

