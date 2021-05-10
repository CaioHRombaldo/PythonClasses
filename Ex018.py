from math import radians, sin, cos, tan

degress = float(input('Enter an angle to calculate your Sine Cosine and Tangent: '))
angle = radians(degress)
print('The angle {} has:\nSen: {:0.2f}\nCos: {:0.2f}\nTan: {:0.2f}'.format(degress, sin(angle), cos(angle), tan(angle)))
