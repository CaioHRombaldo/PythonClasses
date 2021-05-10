year = int(input('Enter a year to see if it is leap or not: '))

if year % 4 == 0:
    print('True, the year {} is a leap year.'.format(year))
else:
    print('False, the year {} is not a leap year.'.format(year))
