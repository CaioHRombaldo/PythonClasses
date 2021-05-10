print('Enter the length of 3 lines and find out if it is possible to form a triangle.')
line1 = int(input('line 1: '))
line2 = int(input('line 2: '))
line3 = int(input('line 3: '))

if line1 + line2 > line3 and line1 + line3 > line2 and line2 + line3 > line1:
    print('TRIANGLE! They can form a triangle.')
else:
    print('FALSE! They cannot form a triangle.')

