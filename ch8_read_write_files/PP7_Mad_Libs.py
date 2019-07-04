#               Automate the Boring Stuff with Python 3
#               Ch 8 -  Practice Project - Mad Libs

#               By Scott Watson

'''
Create a Mad Libs program that reads in text files and lets the user add their
own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file.
For example, a text file may look like this:
'''
import re

# Opens input file, saves it to a string, and closes the file
with open("file.txt", "r+") as file:
    string = file.read() # # Reads file to a string
string
# Defines the patterns to match
adjRegex = re.compile(r'ADJECTIVE')
verbRegex = re.compile(r'(VERB)') # Matchs VERB with AD
adverbRegex = re.compile(r'ADVERB')
nounRegex = re.compile(r'NOUN')

verbRegex.search(string)

search = True # Starts while loop
while search == True:
    if adjRegex.search(string) != None: # Checks if there is a match
        adj= input('Enter an adjective:') # User input to replace the match
        # Next line omits the match ADJECTIVE and replaces with user input stored in adj var
        string = string[:adjRegex.search(string).start()] + adj + string[adjRegex.search(string).end():]
    elif nounRegex.search(string) != None:
        noun = input('Enter a noun:')
        # Next line omits the match NOUN and replaces with user input stored in noun var
        string = string[:nounRegex.search(string).start()] + noun + string[nounRegex.search(string).end():]
    elif verbRegex.search(string) != None:
        verb = input('Enter a verb:')
        # Next line omits the match VERB and replaces with user input stored in verb var
        string = string[:verbRegex.search(string).start()] + verb + string[verbRegex.search(string).end():]
    elif adverbRegex.search(string) != None:
        adverb = input('Enter an adverb:')
        # Next line omits the match ADVERB and replaces with user input stored in adverb var
        string = string[:adverbRegex.search(string).start()] + adverb + string[adverbRegex.search(string).end():]
    else:
        break # Breaks while loop once all matches have been replaced.

print('\n*************', '\n\n',string,'\n\n','*************','\n\n') # prints the mad lib

# Writes mad lib to a new file and closes it
with open('mad_lib.txt', 'w') as madLib:
    madLib.write(string)
print('The mad lib was saved to a new file')



# # REV 1
## This approach failed with the VERB as it had a . at the end and didn't match exactly

# words = file.read().split(" ")# Splits up the words in the text by " " and converts to list

# for word in words: # parses each word from a list of words
#     # Checking if word is adjective, noun, verb, or adverb
#     if  word == 'ADJECTIVE':
#         adjective = input("Enter an adjective:") #User input to replace adjective
#         string += adjective + " " #Appends the list if ADJECTIVE is found
#         continue # Skips back to the top of the loop
#     elif word == 'NOUN':
#         noun = input("ENter a noun:")
#         string += noun + " "
#         continue
#     elif word == 'VERB':
#         verb = input("Enter a verb:")
#         string += verb + " "
#         continue
#     elif word == 'ADVERB':
#         adverb = input("Enter an adverb:")
#         string += adverb + " "
#         continue
#     string += word + " " # This is only run if the replacement keywords are not hit
