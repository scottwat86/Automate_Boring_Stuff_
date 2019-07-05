# Loop through some code to input cat names and print out a response

catNames = [] # creates an empty list
while True: # creates an infinite loop
    print('Enter the name of cat ' + str(len(catNames)+1) + '\n(Or enter nothing to stop.):')
    name = input()
    if name  == '':
        break # breaks out of loop based on user input ''
    catNames +=  [name] # list concatenation
    # If you don't [] name it will take each char and added it seperately to the list
print('The cat names are')
for name in catNames:
    print('  ' + name)

# Data above is structured and more flexible to deal with
