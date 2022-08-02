base=2
exponent=8
coefficents=[3,1,0,2]
def expanded_synthetic_division(dividend, divisor):
    """Fast polynomial division by using Expanded Synthetic Division. 
    Also works with non-monic polynomials.

    Dividend and divisor are both polynomials, which are here simply lists of coefficients. 
    E.g.: x**2 + 3*x + 5 will be represented as [1, 3, 5]
    """
    out = list(dividend)  # Copy the dividend
    normalizer = divisor[0]
    for i in range(len(dividend) - len(divisor) + 1):
        # For general polynomial division (when polynomials are non-monic),
        # we need to normalize by dividing the coefficient with the divisor's first coefficient
        out[i] /= normalizer

        coef = out[i]
        if coef != 0:  # Useless to multiply if coef is 0
            # In synthetic division, we always skip the first coefficient of the divisor,
            # because it is only used to normalize the dividend coefficients
            for j in range(1, len(divisor)):
                out[i + j] += -divisor[j] * coef

    # The resulting out contains both the quotient and the remainder,
    # the remainder being the size of the divisor (the remainder
    # has necessarily the same degree as the divisor since it is
    # what we couldn't divide from the dividend), so we compute the index
    # where this separation is, and return the quotient and remainder.
    separator = 1 - len(divisor)
    return out[:separator], out[separator:]  # Return quotient, remainder.
#def f(j,base=7):
#	return (2*j*j+j+3)%base
#expanded_synthetic_division
def polynomial_multiplication(P, Q,thebase):
    m = len(P)
    n = len(Q)
    result = [0]*(m+n-1)
    for i in range(m):
        for j in range(n):
            result[i+j] += P[i]*Q[j]
            result[i+j] %=thebase
    return result
# function that print polynomial
def polynomial(poly):
    n = len(poly)
    for i in range(n): 
        print(poly[i], end = "")
        if (i != 0): 
            print("x^", i, end = "") 
        if (i != n - 1): 
            print(" + ", end = "")
# polynomial in array representation
P = [2, 3, 0, 4]
print("First polynomial is:")
polynomial(P)
print('\n')
Q = [1, 2, 4, 5]
print("Second polynomial is: ")
polynomial(Q)
print('\n')
result = (polynomial_multiplication(P, Q,base))
print("Product of polynomials is: ")
polynomial(result)

def polynomialProduct(p1,p2,fieldbase):
	# all products are modulo the underlying base.
	#print(p1,p2,fieldbase)
	#print(len(p1), len(p2))
	#print(p1.index)
	return
	
def syntheticDivision(irreduciblePoly, theProduct):
	#return the remainder.
	return 
def int2polynomial(theint,thebase,theexponent):
	extended=thebase**theexponent
	curtheint=theint
	theList=[]
	#convert to a comprehension
	while extended>1:
		extended=int(extended/thebase)
		#print(extended)
		theList.append(int(curtheint/extended))
		curtheint=curtheint%extended
		#print(curtheint)
	theList.reverse()
	#print(theList,"done.")
	return theList

def product(poly1,poly2):
	print(poly1)
	print(poly2)
		
def f(j,thebase):
	return (2*j*j+j+1)%thebase
poly=(list(range(base)))
print (poly)
res=[f(i,base) for i in poly]
print (res)
int2polynomial(44,base,exponent)
int2polynomial(44,2,8)
int2polynomial(320,2,8)
print(int2polynomial(32743,4,16))
#13333213
for i in range(base**exponent):
	for j in range(base**exponent):
	#print(i)
	    print(i, j,polynomial_multiplication(int2polynomial(i,base,exponent),int2polynomial(j,base,exponent),base))
	    #expanded_synthetic_division(int2polynomial(i,base,exponent),int2polynomial(j,base,exponent))
