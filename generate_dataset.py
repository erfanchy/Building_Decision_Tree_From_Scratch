from sklearn.datasets import make_friedman1 
from sklearn.model_selection import train_test_split

def make_data() : 

	X,y = make_friedman1(n_samples = 1000, n_features = 9, noise = 1 , random_state = 100) 

	return train_test_split(X,y,test_size = 0.75,random_state = 3)