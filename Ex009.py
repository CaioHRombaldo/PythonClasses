print('='*40)
n = int(input('Please enter a number to see your multiplication table: '))
print('='*40)
count = 0
while count < 10:
    count += 1
    print('{:^3} x {:^3} = {}'.format(n, count, n*count))
print('='*40)