print('Please enter 3 numbers to check which is the largest and which is the smallest.')
n1 = int(input('Number 01: '))
n2 = int(input('Number 02: '))
n3 = int(input('Number 03: '))

if n1 > n2 and n1 > n3:
    if n2 > n3:
        print('In ascending order: n1: {} n2: {} n3: {}'.format(n1, n2, n3))
    else:
        print('In ascending order: n1: {} n3: {} n2: {}'.format(n1, n3, n2))
elif n2 > n1 and n2 > n3:
    if n1 > n3:
        print('In ascending order: n2: {} n1: {} n3: {}'.format(n2, n1, n3))
    else:
        print('In ascending order: n2: {} n3: {} n1: {}'.format(n2, n3, n1))
else:
    if n1 > n2:
        print('In ascending order: n3: {} n1: {} n2: {}'.format(n3, n1, n2))
    else:
        print('In ascending order: n3: {} n2: {} n1: {}'.format(n3, n2, n1))
