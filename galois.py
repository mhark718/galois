base=7
exponent=2
coefficents=[3,1,0,2]
#def f(j,base=7):
#	return (2*j*j+j+3)%base
def int2polynomial(theint,thebase,theexponent):
	extended=thebase**theexponent
	remaining=theint
	curtheint=theint
	theList=[]
	while extended>1:
		extended=int(extended/thebase)
		#print(extended)
		theList.append(int(curtheint/extended))
		curtheint=curtheint%extended
		#print(curtheint)
	print(theList,"done.")
	
def f(j,thebase):
	return (2*j*j+j+1)%thebase
poly=(list(range(base)))
print (poly)
res=[f(i,base) for i in poly]
print (res)
int2polynomial(44,base,exponent)
int2polynomial(44,2,8)
int2polynomial(320,2,8)
int2polynomial(32743,4,16)
#13333213

