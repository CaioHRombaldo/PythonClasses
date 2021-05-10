catOp = float(input('What is the size of the opposite side of the triangle? '))
catAd = float(input('What is the size of the adjacent side of the triangle? '))
hypotSquare = (catOp ** 2 + catAd ** 2) ** (1/2)
print('The size of the hypotenuse is: {:.2f}'.format(hypotSquare))
