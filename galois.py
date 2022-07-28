base=7
exponent=2
coefficents=[3,1,0,2]
#def f(j,base=7):
#	return (2*j*j+j+3)%base
def f(j,thebase):
	return (2*j*j+j+1)%thebase
poly=(list(range(base)))
print (poly)
res=[f(i,base) for i in poly]
print (res)