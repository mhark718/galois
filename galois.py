base=7
exponent=5
coefficents=[3,1,0,2]
#def f(j,base=7):
#	return (2*j*j+j+3)%base
def polynomialProduct(p1,p2,fieldbase):
	# all products are modulo the underlying base.
	
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
	for j in range(base*exponent):
	#print(i)
	    product(int2polynomial(i,base,exponent),int2polynomial(j,base,exponent))
