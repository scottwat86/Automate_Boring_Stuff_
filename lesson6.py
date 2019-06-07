#               Python Cookbook
#               Chapter 6 - While Loops

# CTRL - C to escape an  infinite loop
# While Loops are used to loop an unknown number of times.

spam = 0
while spam < 5: # Loops through block until condition is met
  print("Hello world!")
  # spam = spam + 1
  spam += 1 # this is more efficient from a computation stand point

# Input Validation -> Repeats until user has entered valid input
name = ''
while name != 'Your Name':
    print('Please type 'Your Name'.')
    name = input()
print('Thank You!')

name = ""
while True:
    print("Enter your name.")
    name = input()
    if name == "Your Name":
        break
print("Thank you!")

spam = 0
while spam < 5:
    spam += 1
    if spam == 3:
        continue # returns to the beginning of the block
    print("spam is:" + str(spam)) # Note that 3 is missing from output b/c of continue
