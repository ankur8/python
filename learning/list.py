squares=[1,4,9,16,25]
print(squares)
print(id(squares[0]))
print(squares[-1])
print(squares[-3:])

#All slice operations return a new list containing the requested elements. This means that the following slice returns a new (shallow) copy of the list:
print(squares[:])     # slice returns shallow copy
a=squares + [36, 49, 64, 81, 100]

print(a)

a[2:4]=[1,4,3]   #Assignment to slices is also possible, and this can even change the size of the list or clear it entirely:
print(a)

#nesting list

a=[1,3,4]
b=['a','b']
x=[a,b]

print(x[0][1])
#***************************

print([1,2,3] * 3)    #multiplication operator
#**************************
words=["ankur","jain","wo","e","newtech"]
for w in words[:]:    #If you need to modify the sequence you are iterating over while inside the loop (for example to duplicate selected items), it is recommended that you first make a copy. Iterating over a sequence does not implicitly make a copy. The slice notation makes this especially convenient:
    if len(w) > 2:
        words.insert(0,w)

print(words)

#************************ range()

for i in range(5):
    print(i)

#start and stop value
for i in range(5,10):
    print('{:=10}'.format(i))

#with stepping
for i in range(5,10,3):
    print('{:>20}'.format(i))


# To iterate over the indices of a sequence in list       <IMPORTANT>

for i in range(len(words)):
    print(i,words[i])


#The function list() is another; it creates lists from iterables:

print(list(range(5)))

#***********

#to delete elemement from list another way i.e by assigning empty list to slice

##my_list[2:5] = []

#List Comprehension: Elegant way to create new List

#####pow2 = [2 ** x for x in range(10)]
# Output: [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]

#This code is equivalent to

pow2 = []
for x in range(10):
   pow2.append(2 ** x)
print(pow2)


my_list = ['p','r','o','b','l','e','m']

# Output: True
print('p' in my_list)

# Output: False
print('a' in my_list)

# Output: True
print('c' not in my_list)

########## implement list as queue better use dequeu as insertion in  beginging is slow in list

from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
queue.popleft()                 # The first to arrive now leaves

queue.popleft()                 # The second to arrive now leaves

print(queue)                         # Remaining queue in order of arrival

##############################

