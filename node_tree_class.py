import numpy as np 

class Tree_Node : 

	def __init__(self,X,y,depth) :

		self.X = X 
		self.y = y 
		self.depth = depth

		self.g = None #Prediction Function
		
		self.j = None # Best Split Parameters
		self.xi = None 
		
		self.left = None # Left branch
		self.right = None # Right Branch

	def Calculate_Loss(self) : 

		if len(self.y) == 0 : 
			return 0 

		return np.sum(np.power(self.y-self.y.mean(),2))