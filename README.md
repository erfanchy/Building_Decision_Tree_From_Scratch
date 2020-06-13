# Building_Decision_Tree_From_Scratch

Built a Decision Tree for a regression problem from scratch without the use of any librairies.
The only time Scikit-Learn was used was to generate a dataset and to use the "train_test_split" to separate the training and testing data. The termination criteria was a maximum depth of 13 after which the MSE (mean squared error) was calculated. For a sanity check, the DecisionTreeRegressor method from scikit-learn was used to also calculate the MSE. The results were very similar.   

1. Clone the repository 
2. Run main.py for MSE results of the tree built from scratch 
3. Run sanity_check.py for MSE results of Scikit-Learn's Decision Tree Model 
