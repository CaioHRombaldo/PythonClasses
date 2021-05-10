name = input('Please enter your name to review: ')

if 'SILVA' in name.upper():
    print('The name "{}" contains "Silva".'.format(name))
else:
    print('The name "{}" does not contain "Silva".'.format(name))
