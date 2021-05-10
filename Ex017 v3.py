import math

catOp = float(input('What is the size of the opposite side of the triangle? '))
catAd = float(input('What is the size of the adjacent side of the triangle? '))
Hyp = math.hypot(catOp, catAd)
print('The size of the hypotenuse is: {:.2f}'.format(Hyp))
