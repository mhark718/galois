def f(j,base=7):
	return (2*j*j+j+3)%base
poly=(list(range(7)))
print (poly)
res=[f(i) for i in poly]
print (res)