#               Python Cookbook
#               Chapter 7 - For Loops

# For loops are used when you need loop a certain number of times
print('My name is:')
for i in range(5):
    print('Scott Watson ' + str(i))

total = 0
for num in range(101): # provides an iterable [0:101] 101 is noninclusive
    total += num
print(total)

i = 0
total = 0
while i < 101:
    total += i
    i += 1
print(total)


for i in range(0, 101, 2): # Start, Stop, Step,
    print(i)
