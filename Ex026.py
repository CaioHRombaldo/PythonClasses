phrase = input('Please enter a sentence to do the analysis: ')

numberOfA = phrase.upper().count('A')
firstA = phrase.upper().find('A') + 1
lastA = phrase.upper().rfind('A') + 1

print('In the phrase "{}" appear {} letters "A".'.format(phrase, numberOfA))
print('The letter "A" appears for the first time in the position: {}.'.format(firstA))
print('The letter "A" appears for the last time in the position: {}.'.format(lastA))
