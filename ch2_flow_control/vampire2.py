# Program defines age and name variables and conducts some conditional
# testing on the variables and responds base on results

name = 'Dracula'
age = 4_000
if name == 'Alice':
    print('Hello Alice ')
elif age <12:
    print('You are not Alice, kiddo')
elif age > 2000:
    print('Unlike you, Alice is not an undead, immortal')
elif age > 100:
    print('You are not Alice, grannie.')
