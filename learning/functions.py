def my_function():
    print("Hello From My Function!")

def my_function_with_args(username, greeting):
    print("Hello, %s , From My Function!, I wish you %s"%(username, greeting))

def sum_two_numbers(a, b):
    return a + b

# print(a simple greeting)
my_function()

#prints - "Hello, John Doe, From My Function!, I wish you a great year!"
my_function_with_args(str(10), "a great year!")

# after this line x will hold the value 3!
x = sum_two_numbers(int("1"),2)
print(x)

##########################


def list_benefits():
    return "More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"

# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(benefit):
   # return "%s is a benefit of functions!" % benefit
    #print(f"{benefit} is ")
    return f"{benefit} is a benefit of functions!"

def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    #print(list_benefits())
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()

################## Default arguments ##############
def ask_ok(prompt:str, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

#####################################

#Important warning: The default value is evaluated only once. This makes a difference when the default is a mutable object such as a list, dictionary, or instances of most classes. For example, the following function accumulates the arguments passed to it on subsequent calls:

def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))
#This will print

#[1]
#[1, 2]
#[1, 2, 3]
#If you don’t want the default to be shared between subsequent calls, you can write the function like this instead:
print("*"*20)
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L
print(f(11))
print(f(22))


#################### arbitrary argument list
#Normally, these variadic arguments will be last in the list of formal parameters, because they scoop up all remaining input arguments that are passed to the function. Any formal parameters which occur after the *args parameter are ‘keyword-only’ arguments, meaning that they can only be used as keywords rather than positional arguments.

def concat(*args, sep="/"):
    return sep.join(args)

print(concat("earth", "mars", "venus"))

print(concat("earth", "mars", "venus", sep="."))

################### unpacking arguments

#def unpack()
print(list(range(2,6)))  #normal call with separate arguments
list1=(2,6)

print(list(range(*list1)))

### another unpacking example
def amt(p,r,t):
    return p*r*t/100

d=[1000,10,2]
print("SI= ",amt(*d))

###### for passing dictonary for unpacking
def parrot(voltage, state='a stiff', action='voom'):
    print(state,voltage+"2",action)

d={"voltage":"200","state":"statevalue","action":"no"}
parrot(**d)
################## lambda function

def incrementor(n:str):
    print("annotion",incrementor.__annotations__)
    return lambda x,y: x +n+y

print(incrementor(10))

f=incrementor(10)
#print(f)
print(f(2,2))


####### lambda functon can have many arguments and one expression only and return function object
#lambda argument: manipulate(argument)/expression

add=lambda x,y:x+y   # lambda function has no name . it returns function object which gets assigned to add

print("LAMBDA",add(3,3))
##########################
xx=99

def func() :
     #xx=xx+1000  # error
     global xx
     xx=xx+100
     print(xx) #1000

func()
print(xx)  #99