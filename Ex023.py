number = input('Enter a number from 0 to 9999 to analyze: ')

if len(number) > 0:
    u = number[len(number) - 1]
else:
    u = 0
if len(number) > 1:
    t = number[len(number) - 2]
else:
    t = 0
if len(number) > 2:
    h = number[len(number) - 3]
else:
    h = 0
if len(number) > 3:
    m = number[len(number) - 4]
else:
    m = 0

print('Unit: {}\nTens: {}\nHundred: {}\nThousand: {}'.format(u, t, h, m))
