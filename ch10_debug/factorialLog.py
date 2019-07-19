import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')

# logging.diable(logging.CRITICAL)   # Disables logging below

def factorial(n):
    logging.debug('Start of factorial(%s)' % (n))
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(%s)' % (n))
    return total

print(factorial(5))
logging.debug('End of program')

'''OUTPUT
 2019-07-15 22:06:19,443 - DEBUG - Start of program
 2019-07-15 22:06:19,445 - DEBUG - Start of factorial(5)
 2019-07-15 22:06:19,446 - DEBUG - i is 0, total is 0
 2019-07-15 22:06:19,447 - DEBUG - i is 1, total is 0
 2019-07-15 22:06:19,448 - DEBUG - i is 2, total is 0
 2019-07-15 22:06:19,449 - DEBUG - i is 3, total is 0
 2019-07-15 22:06:19,450 - DEBUG - i is 4, total is 0
 2019-07-15 22:06:19,451 - DEBUG - i is 5, total is 0
 2019-07-15 22:06:19,452 - DEBUG - End of factorial(5)
 2019-07-15 22:06:19,452 - DEBUG - End of program
0
'''
