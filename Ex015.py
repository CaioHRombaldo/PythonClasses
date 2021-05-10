print('=--Car rental calculator--=')
coveredKM = float(input('How many km were covered? '))
daysRented = float(input('How many days was it rented? '))
priceToPay = daysRented * 60 + coveredKM * 0.15
print('The amount to be paid is US${:.2f}'.format(priceToPay))

