import re

s='this is 1234 8968'

#re.sub(patter,replacement,string
#\d is for digit
#\D is for non-digit

p=re.sub('\d*','',s)
n=re.sub('\D*','',s)
print(p)
print(n)