number = int(input('Enter a number from 0 to 9999 to analyze: '))

u = number // 1 % 10
t = number // 10 % 10
h = number // 100 % 10
m = number // 1000 % 10

print('Unit: {}\nTens: {}\nHundred: {}\nThousand: {}'.format(u, t, h, m))
