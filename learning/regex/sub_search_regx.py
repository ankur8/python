import re
#https://www.youtube.com/watch?v=hvo1XACSNcw&list=PLy-CGmBdq2VFclPZZRTC5wqV6sKM4WOaI&index=60

s='abc.xys@d.com'
#\w word character
a='this is a 1234 4567'


p=re.search('\w+\.*\w+@\w+\.\w+',s)

x=re.sub('\w+s','$',a)  # replace word ending with s i.e \w+s   so this is is replaced with dollar
print(p.group())

print(x)