salary = float(input('Please enter your salary to calculate the increase US$: '))

if salary >= 1250.0:
    increase = 10
else:
    increase = 15

increased = salary * increase / 100
newSalary = salary + increased

print('The increase will be: {}%\nThe Salary US$: {:.2f} with an'
      ' increase of US$: {:.2f} will be US$: {:.2f}'.format(increase, salary, increased, newSalary))
