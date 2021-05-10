print('=-------=SPEEDOMETER=-------=')
speed = float(input('Please enter vehicle speed Km/h: '))
limit = 80.0

if speed > limit:
    print('FINED!\nSpeed above the limit.')
    fine = 7 * (speed - limit)
    print('The total fine to be paid is US$:{:.2F}'.format(fine))
else:
    print('OK!\nSpeed within the expected limit.')

print('=-----=Have a good day!=-----=')
