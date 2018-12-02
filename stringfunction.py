import re
s=" ankur 12345"

#find function
print(s.find("12345"))

# Join function

a=['ab','cd']
b=';'
print(b.join(a))   #join
print(';'.join(a))  #join same as above using conventional programming aproach

print(s.split(" "))

for n in range(2,4):
    print("hi",n)