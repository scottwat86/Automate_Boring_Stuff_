##               Automate the Boring Stuff with Python 3
#               Lesson 14 -
#                   for loop with lists
#                   multiple assignment
#                   augmented assignments operators

# RECAP
# For loops technically iterate over the values in a list

# The range() function returns a list like value which
# can be passed to the list() function if you need an actual list value

# variables can swap their values using multiple assignment

# augmented assignment operator like += used as shorcuts
# They are also faster at run time than 1+1


for i in range(4):
    print(i)

range(4) # range(0, 4)

for i in [0,1,2,3]:
    print(i)

spam = list(range(0,100,2))

# supplies = ['pens', 'staplers', 'flame-throws', 'binders']
supplies = 'pens-' *16
supplies = supplies.split(sep='-')
for i in range(len(supplies)):
    print('Index ' + str(i) + " in supplies is: " + supplies[i])

cat = ['fat', 'orange', 'loud']
size = cat[0]
color = cat[1]
disposition = cat[2]

size, color, disposition = cat # unpacks list to the Variables

size, color, disposition = 'skinny', 'black', 'quiet'
a = 'AAA'
b = 'BBB'
a, b = b, a

spam = 42
spam = spam +1 # 43
spam +=1 # 44
