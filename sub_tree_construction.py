from best_split_ import best_split
from data_split_ import DataSplit
import numpy as np 
from node_tree_class import Tree_Node

def Construct_Sub_Tree(node,max_depth) :

    if node.depth == max_depth or len(node.y) == 1 : 
        node.g = node.y.mean()
    else : 
        j,xi = best_split(node)
        node.j = j 
        node.xi = xi 
        Xt,yt,Xf,yf = DataSplit(node.X,node.y,j,xi)

        if len(yt) > 0 : 
            node.left = Tree_Node(Xt,yt,node.depth+1)
            Construct_Sub_Tree(node.left,max_depth)

        if len(yf) > 0 : 
            node.right = Tree_Node(Xf,yf,node.depth+1)
            Construct_Sub_Tree(node.right,max_depth)
