def addition(a1,a2):
    return a1+a2

def sub(a1,a2):
    return a1-a2

def mul(a1,a2):
    return a1*a2

def division(a1,a2):
    return a1/a2



print("1 for addition")
print("2 for substraction")
print("3 for multiplication")
print("4 for division")

choice=input("Press choice: ")
num1=int(input("enter first number "))
num2=int(input("enter second number "))
if choice == '1':
    print("sum of two number is :",addition(num1,num2))
elif choice == '2' :
    print("substraction result",sub(num1,num2))
elif    choice == '3' :
    print("Multiplication result",mul(num1,num2))
elif choice == '4' :
    print("division result",division(num1,num2))
else:
    print("Invalid input")

