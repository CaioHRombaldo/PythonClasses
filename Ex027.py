name = input('Please enter your name to review: ')

firstName = name.split()[0]
lastName = name.split()[len(name.split()) - 1]

print('Name: {}\nFirst Name: {}\nLast Name: {}'.format(name, firstName, lastName))
