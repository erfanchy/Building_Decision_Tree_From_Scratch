def DataSplit(X,y,j,xi) :
	ids = X[:,j]<=xi 
	Xt = X[ids == True,:]
	Xf = X[ids==False,:]
	yt = y[ids==True]
	yf = y[ids==False] 
	return Xt,yt,Xf,yf 
	