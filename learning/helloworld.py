print("hello world")
a = """hi ankur"""
b="ankur"[3]
print (b)  #print
print(len(a)) #length of a string
n=102
print(str(n)+"1")   #string to number conversion

print (a.upper()) #upper case
print ("wowpythoN".upper()) #upper case conversion

#del a #delete ref of variable a like unset in shell

print("ns is",n) #print var vaule with string separated by comma

print(10//3)  #to pick only int part

c=a+b;
print (c,n)  #n value is printed after space due to comma . each c and n is an object.

print("""ankur is 
      a boy """)    #multiline string literal with triple quotes single or double either work
b='new\
next'   #multilne string literal with backspace for new line...
#below is error to resolve us + operator
#print(b "new")   #concatinating variable and string litrel error to resolve use + operator print (b+"new")


print(b.upper())
print('1,2,3'.split(','))

print('  1,2,,3 '.split(',',4))
print(' 1 2 3 '.split())
name='ankur'
print(f'he is my {name}')
print('{:_<15}'.format(name),'new','{:<15}'.format('test1'))
print(name.find("an"))  #find string in str return index else -1

person = {'first': 'Jean-Luc', 'last': 'Picard'}  #dictionary
x = 1
y = 2

# TODO: change this code
x_list = [x] * 10
y_list = [y]
big_list = []

print(f"x_list contains {len(x_list)}  objects" )


x=int(input("enter any number"))
if x<0:
    x=0
    print("Negative changed to zero")
elif x==0:
    print('Zero')
elif x==1:
    print('Single')
else:
    print('More')
print('hi')   #indentation this print is not under else statement but outside if constructs
