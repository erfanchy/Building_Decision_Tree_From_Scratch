def predict(X,node) :

	if node.right== None and node.left!= None : 
		return predict(X,node.left)

	if node.left == None and node.right != None :
		return predict(X,node.right) 

	if node.right==None and node.left==None : 
		return node.g 

	else : 
		if (X[node.j] <=node.xi) : 
			return predict(X,node.left)

		else : 
			return predict(X,node.right)