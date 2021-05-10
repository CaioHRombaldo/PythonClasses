cityName = str(input('Please enter the name of your city to review: '))
firstWordCityName = cityName.split()[0]

if firstWordCityName.upper() == "SANTO":
    print('The city {} starts with "Santo".'.format(cityName))
else:
    print('The city {} does not start with "Santo".'.format(cityName))
