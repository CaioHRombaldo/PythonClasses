km = float(input('Please enter how many kilometers you want to travel to calculate the fare: '))

if km <= 200:
    fare = 0.50 * km
else:
    fare = 0.45 * km

print('To travel {} Km your ticket will cost US$:{:.2f}'.format(km, fare))
