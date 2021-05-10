import re

name = input('Please enter your name to review: ')

if re.search('\\bsilva\\b', name, re.IGNORECASE):
    print('The name "{}" contains "Silva".'.format(name))
else:
    print('The name "{}" does not contain "Silva".'.format(name))
