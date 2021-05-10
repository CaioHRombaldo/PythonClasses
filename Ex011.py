height = int(input('Please enter the height of the wall in meters: '))
width = int(input('Please enter the width of the wall in meters: '))
area = height * width
paintByArea = 2
print('It will take {} liters of paint to paint the entire wall.'.format(area/paintByArea))
