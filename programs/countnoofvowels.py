# Program to count the number of each vowel in a string
#important part {}.fromkeys to create dictionary
vowels = 'aeiou'
ip_str = 'Hello, have you tried our channel section yet?'
ip_str=ip_str.casefold()

# make a dictionary with each vowel a key and value 0
count={}.fromkeys(vowels,0)

print(count)


for str in ip_str:
    if str in count:
        count[str]+=1

print(count)


X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

print(len(X))

#We use the dictionary method fromkeys() to construct a new dictionary with each vowel as its key and all values equal to 0. This is initialization of the count
#In each iteration we check if the character is in the dictionary keys (True if it is a vowel) and increment the value by 1 if true.
