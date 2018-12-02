import re
#*?, +?, ??
#The '*', '+', and '?' qualifiers are all greedy;
# they match as much text as possible. Sometimes this behaviour isn’t desired;
# if the RE <.*> is matched against <a> b <c>, it will match the entire string, and not just <a>.
# Adding ? after the qualifier makes it perform the match in non-greedy or minimal fashion; as few characters as possible
# will be matched. Using the RE <.*?> will match only <a>.
#https://docs.python.org/2/library/re.html?highlight=matching%20searching#regular-expression-syntax
a="Today is wednesday and tomorrow is thrusday"
#re.search(pattern,string,flags<optional>)
#re.I flag means case insensitive
p=re.search('.*and.*',a)
s=re.search('(.*)and(.*)',a)
t=re.search('(.*) wednesday And (.*) thrusday',a,re.I)
x=re.search('(.*) wednesday (And) (.*) thrusday',a,re.I)
y=re.match('Today.*',a)
if p:
    print("Found: ",p.group(),"\n\n")
else:
    print("NOT FOUND")


print('group 1: ',s.group(1),':',s.group(1).capitalize())   #printing only first group matched by (.*) before and
print('group 2: ',s.group(2),":",s.group(2).capitalize())   #printing second group only after and matched by (.)

print(t.group(1),t.group(2))
print(x.group(2))
print(y.group())