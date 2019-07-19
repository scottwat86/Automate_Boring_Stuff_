#               Automate the Boring Stuff with Python 3
#               Ch 10 -  Debugging

#           EXCEPTIONS
# Python raises an exception whenever it tries to execute invalid code.
# Exceptions are raised by a "raise" statement
# raise statement consists of raise keyword, Exception() call, and a helpful string passed
#The traceback is displayed by Python whenever a raised exception goes unhandled

# See boxPrint.py

#                   TRACEBACK AS A STRING
# traceback includes the error message, the line number of the error cause, and the sequence of the
# function calls that led to the error. The sequence is called a call stack

# See errorExample.py

import traceback

try:
    raise Exception('This is the error message.')
except:
    errorFile = open('errorInfo.txt', 'w')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The traceback info was written to errorInfo.txt')

#                   ASSERTIONS
# Assertions are a sanity check to ensure that the code isn't doing something completely wrong
# performed with an assert statement
# if the statement fails then an AssertionError is raised
# If an assert statement fails the program crashes

#                   DISABLING ASSERTIONS
# Can be disabled by passing "-o" when running python
# This is useful once testing is complete and you dont want it to slow down the code
# assert are for TESTING not final product

podBayDoorStatus = 'open'
assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'
podBayDoorStatus = 'I\'m sorry, Dave. I\'m afraid I can\'t do that.'
assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'

''' OUTPUT
---------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)
<ipython-input-19-468777bd330f> in <module>()
----> 1 assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'

AssertionError: The pod bay doors need to be "open".
'''

#                   USING AN ASSERTION IN A TRAFFIC LIGHT SIMULATION
market_2nd = {'ns': 'green', 'ew': 'red'}
mission_16th = {'ns': 'red', 'ew': 'green'}

def switchLights(stoplight):
    for key in stoplight.keys():
        if stoplight[key]  == 'green':
            stoplight[key] = 'yellow'
        elif stoplight[key] == 'yellow':
            stoplight[key] = 'red'
        elif stoplight[key] == 'red':
            stoplight[key] = 'green'
        assert 'red' in stoplight.values(), 'Neither light is red!' + str(stoplight)

switchLights(market_2nd)

'''
---------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)
<ipython-input-27-70f8ee039cec> in <module>()
     12         assert 'red' in stoplight.values(), 'Neither light is red!' + str(stoplight)
     13
---> 14 switchLights(market_2nd)

<ipython-input-27-70f8ee039cec> in switchLights(stoplight)
     10         elif stoplight[key] == 'red':
     11             stoplight[key] = 'green'
---> 12         assert 'red' in stoplight.values(), 'Neither light is red!' + str(stoplight)
     13
     14 switchLights(market_2nd)

AssertionError: Neither light is red!{'ns': 'yellow', 'ew': 'green'}
'''

#                   LOGGING
# logging module
# Using the logging module

#               DISABLING LOGGING
#       logging.disable(logging.CRITICAL)

# See factorialLog.py

import logging
logging.basicConfig(level=logging.DEBUG,
                                  format=' %(asctime)s - %(levelname)s - %(message)s')

logging.debug('Start of program')

logging.diable(logging.CRITICAL) # Disables logging

#               LOGGING LEVELS

#           DEBUG            logging.debug()         lowest level, used for small details
#           INFO                logging.info()            Used to record info on general events
#           WARNING        logging.warning()    Used to indicate a potential problem in running code
#           ERROR            logging.error()         Used to record an failing error that stops code
#           CRITICAL       logging.critical()      Highest level, Used for fatal errors that stop code

import logging
logging.basicConfig(level=logging.DEBUG,
                                   format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Some debugging details.')
logging.info('The logging module is working.')
logging.warning('An error message is about to be logged.')
logging.error('An error has occured.')
logging.critical('The program is unable to recover.')


#               LOGGING TO A FILE
import logging, os
path = os.getcwd() +'\\myProgramLog.txt'
print(path)
logging.basicConfig(filename=path, level=logging.DEBUG,
                                  format='%(asctime)s - %(levelname)s - %(message)s')
logging.critical('The program is unable to recover.')
#                   IDLE DEBUGGER
#               GO button will execute until it terminates or reaches a breaking point
#               STEP button will execute the next line of code
#               OVER button executes similar to STEP but skips over the code within the function and returns the result
#               OUT button executes all code at speed until it returns from the current fuction call
#               QUIT button stops the debugging entirely
#               BREAKPOINTS specific line of code the forces the debuugger to pause


#           SUMMARY
'''
Assertions, exceptions, logging, and the debugger tools to eliminate bugs in code

assert statement are good 'sanity checks' for error that the program shouldnt recover from.
Use assert at the beginning and end of functions to check input/outputs

'''

#               Practice Questions
#           1)
spam =11
assert spam <10
#           2)
spam = 'hello'
eggs = 'HeLlo'
assert spam.lower() != eggs.lower()
#           3)
assert False
#           4)
import logging
logging.basicConfig(level=logging.DEBUG,
                                  format='%(asctime)s - %(levelname)s - %(message)s')
#           5)
import logging
logging.basicConfig(filename=path, level=logging.DEBUG,
                                  format='%(asctime)s - %(levelname)s - %(message)s')
#           6)
'''
   DEBUGGING
   INFO
   WARNING
   ERROR
   CRITICAL
'''
#           7)
logging.disable(logging.CRITICAL)
#           8)
'''Logging can be turned on and off with one line of code and provides a timestamp
and the ability to save results to a file. Print has none debugging uses that can get
mixed up with debugging'''
#           9)
'''
STEP goes line by line through the code
OVER steps over functions whihc run at full speed and skips over the debugger
OUT steps out of function once you have already stepped into a function
'''
#           10)
''' Once GO is clicked, the debugger will stop either at the end of the code or at a breakpoint'''
#           11)
''' BREAKPOINT provides a mark location for the debugger to stop. It is like a checkpoint '''
#           12)
''' Right clicking and clicking BREAKPOINT  '''
