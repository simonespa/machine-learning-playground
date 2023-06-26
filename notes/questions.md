# Questions

## Imputation
Q: Should I run the imputation on the entire dataset, or split it first in train/test, then fit the imputation on the training set only so that the mean calculated on the training data is used for both train and test?
A:
## Data transformation
Q: If we transform the train set only, when we do prediction should the data be transformed too?
A:

## Stratified sampling
Q: When do we use stratifid sampling?
A: For classification problems, when the class is imbalanced. This is because we want to give the model a fair chance to learn correlations for the minority class
