#2
# Create a variable called age.
# Write an if statement, which checks if someone that age is allowed to drink.
# They are only if they're 18 and over.
# If they are allowed - print 'Can drink!'.
# If they are not - print 'You have to wait!'

age=1
if age>=18:
    print("can drink")
else:
    print("can not drink")


#grade = input('Gimme a grade please')
grade='90'
grade = int(grade)

if grade>80:
    print("Distinction")
elif grade>=60:
    print("Pass")
else:
    print("fail")




# Bob is a lackadaisical teenager.
# In conversation, his responses are very limited.
#
# Bob answers 'Sure.' if you ask him a question (with ?).
# He answers 'Whoa, chill out!' if you yell at him (with !).
# He answers 'Calm down, I know what I'm doing!' if you yell a question at him (with ! and ?).
# He says 'Fine. Be that way!' if you don't say anything (an empty string '').
# He answers 'Whatever.' to anything else.



#to_bob = input('What would you like to say to Bob?\n')
to_bob='?'
if '?' in to_bob and '!' in to_bob:
    print('Calm down, I know what I\'m doing!')
elif '?' in to_bob:
    print('Sure.')
elif '!' in to_bob:
    print('Whoa, chill out!')
elif to_bob == '':
    print('Fine. Be that way!')
else:
    print('Whatever.')


