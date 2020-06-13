from data_split_ import DataSplit
from node_tree_class import Tree_Node

def best_split(node) :
	X = node.X 
	y = node.y 
	best_var = 0 
	best_xi = X[0,best_var] 
	best_split_val = node.Calculate_Loss()


	m,n = X.shape

	for j in range(0,n) : 
		for i in range(0,m) : 
			xi = X[i,j]
			Xt,yt,Xf,yf = DataSplit(X,y,j,xi)
			tmpt = Tree_Node(Xt,yt,0)
			tmpf = Tree_Node(Xf,yf,0)
			loss_t = tmpt.Calculate_Loss() 
			loss_f = tmpf.Calculate_Loss()
			curr_val = loss_t + loss_f 
			if curr_val < best_split_val : 
				best_split_val = curr_val
				best_var = j 
				best_xi = xi 
	return best_var,best_xi 