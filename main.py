import numpy as np 
from generate_dataset import make_data
from node_tree_class import Tree_Node
from sub_tree_construction import Construct_Sub_Tree
from best_split_ import best_split
from predict_ import predict

def main() : 

	X_train,X_test,y_train,y_test = make_data() 
	max_depth = 13 #Termination Criterion 
	root = Tree_Node(X_train,y_train,0)  
	Construct_Sub_Tree(root,max_depth)

	y_hat = np.zeros(len(X_test))

	for i in range(len(X_test)) : 

		y_hat[i] = predict(X_test[i],root)

	mean_squared_error = np.mean(np.power(y_hat - y_test,2))
	print ("Loss of manually constructed tree : ", mean_squared_error)

if __name__=="__main__" :

	main()