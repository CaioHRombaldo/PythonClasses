p = float(input('Please enter the product price to see the discount: US$'))
d = 5
print('-'*20)
print('Original value: {:0.2f}\nDiscount percentage: {}%\nDiscount amount: {:0.2f}\nDiscounted value: {:0.2f}'.format(p, d, (p*d/100), p-(p*d/100)))
