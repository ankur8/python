
#https://www.programiz.com/python-programming/string
#https://www.programiz.com/python-programming/methods/string
a='ankur'
print ('A' in "Aa" )

print(tuple(enumerate(a)))

str = 'cold'

# enumerate() return object The enumerate() function returns an enumerate object. It contains the index and value of all the items in the string as pairs. This can be useful for iteration.
list_enumerate = list(enumerate(str))
print('list(enumerate(str) = ', list_enumerate)
print('tuple(enumerate(str) = ', tuple(enumerate(str)))

#character count
print('len(str) = ', len(str))

######## pallendrome string #####

aa="aia"
aa=aa.casefold()
a2 = reversed(aa)
l1=list(a2)
l2=list(aa)

if list(aa) == list(a2):
    print('is palendrome')
else:
    print("not palendrome",)


print(list(aa),l2)

################ split, join, format example on string

list1="This will split all words into a list".split()
print(list1)
print(' '.join(list1))

print("|{:<10}|{:^10}|{:>10}|".format('butter','bread','ham'))
print('Happy New Year'.replace('Happy','Brilliant'))

################ punctuation removing

# define punctuation
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

my_str = "Hello!!!, he said ---and went."

# To take input from the user
# my_str = input("Enter a string: ")

# remove punctuation from the string
no_punct = ""
for char in my_str:
   if char not in punctuations:
       no_punct = no_punct + char

# display the unpunctuated string
print(no_punct)
#####
