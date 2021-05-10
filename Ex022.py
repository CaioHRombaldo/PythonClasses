name = str(input('Plese enter your name to review: '))

print('Your name in capital letters: {}.'.format(name.upper()))
print('Your name in lowercase: {}.'.format(name.lower()))
nameSplit = name.split()
print('Your full name has {} letters.'.format(len(''.join(nameSplit))))
print('Your first name has {} letters.'.format(len(nameSplit[0])))
