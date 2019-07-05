#               magix8Ball2.py
import random

messages = [
'It is certain',
'It is decidedly so',
'Yes definitely',
'Reply haze try again',
'Ask again later',
'Concentrate and ask again',
'My reply is no',
'Outlook not so good',
'Very doubtful']

print(messages[random.randint(0, len(messages)-1)])
