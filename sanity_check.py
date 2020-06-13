from sklearn.tree import DecisionTreeRegressor 
from generate_dataset import make_data
import numpy as np

X_train,X_test,y_train,y_test = make_data() 
regTree = DecisionTreeRegressor(max_depth=10,random_state=0) 
regTree.fit(X_train,y_train)
y_hat = regTree.predict(X_test)
MSE2 = np.mean(np.power(y_hat-y_test,2))
print('DecisionTreeRegressor : tree loss =',MSE2)