# Implementing Euclidean algorithm

import sys
import numpy

def Eu_algo(x,y):
	x0 = max([x,y])
	y0 = min([x,y])
	

	
	while x0 != y0:
		x1 = max([x0-y0,y0])
		y1 = min([x0-y0,y0])
		
		x0 = x1
		y0 = y1
		print x0
		print y0
		
	return x0

input1 = int(sys.argv[1])
input2 = int(sys.argv[2])

gcd = Eu_algo(input1, input2)
print 'Gcd of two inputs is %d' %gcd