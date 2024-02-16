# Questions/Clarifications

## Cross Validation and Grid Search (Random Search)
- Q: As I understood it, cross validation doesn't give me the best model because it is using the same model with the same parameters and it is training "from scratch" every time. Is cross validation a way to evaluate the model variance based on different portions of the dataset being used for training/prediction?
- A:

- Q: Is Grid Search (or Random Search), unlike Cross Validation, a way to fine tune parameters
- A: Yes

## Stratification

- Q: When do we use stratification?
- A: For classification problems, when the class is imbalanced. This is because we want to give the model a fair chance to learn correlations for the minority class and avoid having a training set without minority class.


1) Overfitting even when we have the test set witout the labels?

2) Other than just visualising a pairplot when feasable, is there a numerical test I can run to interpret whether there is a linear or non-linear relationship between features?

3) Cross Validation: is it a way to test the variance, but at the end of the day it doesn't give us the best model

4) When do we do stratification?

lots of classes, very small compared to the others

5) Can we scale time series data before doing the decomposition? It is useful for visualisation, because it brings all the variables on the same scale. Would this also help forecasting models?
